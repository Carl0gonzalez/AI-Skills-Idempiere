---
name: jenkinsfile-developer
description: Guides the creation, updates, and maintenance of Jenkinsfile pipelines for iDempiere 8 plugins, ensuring they include version-matched compilation and README archiving steps.
---

# Purpose

This skill guides the creation and update of Jenkinsfile pipelines for iDempiere 8 OSGi plugin projects. It focuses on ensuring standard compile stages (tailored for iDempiere 8 build environments) and automatically including a stage to parse and archive the `README.md` as a beautiful dark-themed HTML report.

It should be activated when the user asks to:
- Create a new `Jenkinsfile` for an iDempiere 8 plugin
- Update an existing `Jenkinsfile`
- Add build or publishing stages to a plugin's pipeline
- Standardize or improve the documentation publishing (README archiving) in CI/CD

# Operating Principles

1. **Version-Matched Builder (iDempiere 8)**: Discover and use the target-platform builder image and branch compatible with the repository's iDempiere 8 baseline. Do not reuse a builder tag or target-platform branch from another major version.
   - Configure any host Maven-cache mount through a job or environment variable; do not hardcode a host path in the skill or generated pipeline.
2. **Automated Documentation Archiving**: Every `Jenkinsfile` MUST include the `Archive Readme` stage to convert the project's `README.md` to `readme.html` and publish it using Jenkins' `publishHTML`.
3. **Aesthetic Consistency**: The generated `readme.html` must always use the premium dark-themed design system.
4. **Python-Based Generation**: Use a Python 3 alpine image to parse Markdown to HTML inside the Jenkins pipeline, using doubled curly braces (`{{` and `}}`) in CSS blocks since they are defined inside Python f-strings.
5. **Init Stage for Job Descriptions**: Always set `currentBuild.description`. Add branch or multibranch job descriptions only when the existing Jenkins security policy permits access to `currentBuild.rawBuild`; otherwise omit them and report the limitation. When enabled, update parent descriptions only on the configured main branch and derive custom dependencies from the manifest and README.

# Activation Guidance

Trigger this skill for prompts like:
- "create a jenkinsfile for com.cdsoftware.recaptcha"
- "add readme archiving stage to the pipeline"
- "standardize the build pipeline of the payroll plugin"
- "update jenkinsfile to publish html docs"

# Constraints

- **Scope Limit**: Focus on pipeline definitions (`Jenkinsfile`). Do not modify Java sources, manifest files, or project build descriptors (`pom.xml`) unless explicitly requested.
- **Conservative Patching**: When modifying an existing pipeline, prefer minimal, non-destructive, and secure changes. Retain original comments, stage naming, indentation, and structure as much as possible.
- **No Speculative Elements**: Never introduce stage names, environment variables, credentials, checkout folders, or dependencies that are not justified by the existing Jenkinsfile, the repository metadata, or explicit user request.
- **No Secret Exposure**: Do not hardcode credentials, passwords, or tokens. If credentials are required, use standard Jenkins credentials bindings (e.g. `withCredentials` or reference `credentials('id')`) and prompt the user to configure them.
- **Sandbox and Syntax Safety**: Always verify that all Groovy braces `{}` are balanced. Do not call sandbox-restricted APIs such as `currentBuild.rawBuild` unless the existing pipeline already uses them or Jenkins approval is explicitly available.
- **Optimized Inputs and Timeouts**: Avoid calling `input` steps inside stages that lock containerized/heavy execution agents (e.g., docker compile stage). If an `input` is needed, wrap it in a `timeout` block.
- **Python Compatibility**: The python script within the Jenkinsfile must run in standard python:3.9-alpine or similar basic Python images without requiring third-party libraries (e.g. use standard library `re` and basic string operations).
- **CSS Escape Rule**: Always double curly braces `{{` and `}}` in the CSS styles block inside the Python script to avoid f-string parsing issues.
- **Backslash Escaping Rule**: Groovy triple-single-quotes ('''...''') in Jenkinsfiles interpret backslashes. To prevent compilation errors, all regex backslashes must be double-escaped in the final Jenkinsfile (e.g., `\\*\\*`, `\\1`). If you write the Jenkinsfile using a Python generation script, you must escape those backslashes accordingly (e.g., using four backslashes `\\\\` in Python strings).

# Workflow

When creating or updating a `Jenkinsfile`, follow these ordered steps:

1. **Add Init Stage**: Set up the `Init` stage to update the job descriptions for the branch, multibranch parent, and build, including dependency information if any. Ensure that parent job descriptions are only set when building the `master` branch:
   ```groovy
   stage('Init') {
       agent any
       steps {
           script {
               def branchJob = currentBuild.rawBuild.getParent()
               def multibranchJob = branchJob.getParent()

               // Define the list of dependency plugins (statically list them based on checked-out dependencies)
               def dependenciesStr = "com.cdsoftware.payroll, com.cdsoftware.base" // or "None"

               def branchDescription = """
               <b>Plugin:</b> ${env.PLUGIN_NAME}<br/>
               <b>iDempiere:</b> ${env.IDEMPIERE_VERSION}<br/>
               <b>Branch:</b> ${env.BRANCH_NAME ?: 'N/A'}<br/>
               <b>Job:</b> ${env.JOB_NAME}<br/>
               <b>Dependencies:</b> ${dependenciesStr}<br/>
               """

               def mainDescription = """
               <b>Plugin:</b> ${env.PLUGIN_NAME}<br/>
               <b>iDempiere:</b> ${env.IDEMPIERE_VERSION}<br/>
               <b>Repository:</b> Bitbucket<br/>
               <b>Last executed branch:</b> ${env.BRANCH_NAME}<br/>
               <b>Last build:</b> #${env.BUILD_NUMBER}<br/>
               <b>Dependencies:</b> ${dependenciesStr}<br/>
               """

               // Only update parent job and multibranch descriptions for the configured main branch
               if (env.BRANCH_NAME == 'master') {
                   branchJob.setDescription(branchDescription)
                   multibranchJob.setDescription(mainDescription)
               }

               currentBuild.description = "${env.PLUGIN_NAME}-${env.IDEMPIERE_VERSION}.${env.BUILD_NUMBER}"

               echo "Build description and applicable job descriptions updated."
           }
       }
   }
   ```
2. **Add Compile Stage**: Set up the `Compile` stage using target platform builder:
   ```groovy
   stage('Compile') {
       agent {
           docker {
               image "${env.IDEMPIERE_BUILDER_IMAGE}"
               // Optionally set IDEMPIERE_M2_CACHE_MOUNT in Jenkins, for example: -v <host-m2-cache>:/root/.m2
               args "--entrypoint='' -u root:root ${env.IDEMPIERE_M2_CACHE_MOUNT ?: ''}"
           }
       }
       steps {
           dir('target-platform') {
               git branch: env.IDEMPIERE_TARGET_PLATFORM_BRANCH, url: 'https://github.com/ingeint/idempiere-target-platform-plugin.git'
               sh './plugin-builder build ../${PLUGIN_NAME}'
               archiveArtifacts artifacts: "target/${PLUGIN_NAME}-${IDEMPIERE_VERSION}.${BUILD_NUMBER}.jar", fingerprint: true
               // Preserve generated outputs; let workspace cleanup be managed by Jenkins policy.
           }
       }
   }
   ```
3. **Add Archive Readme Stage**: Write the `Archive Readme` stage containing the Python Markdown-to-HTML parser script with the dark-themed styling:
   ```groovy
   stage('Archive Readme') {
       agent {
           docker {
               image 'python:3.9-alpine'
           }
       }
       steps {
           script {
               if (fileExists('README.md')) {
                   writeFile file: 'generate_readme.py', text: '''import sys, re

   def md_to_html(md_text):
       html = []
       in_list = False
       in_code = False
       in_table = False
       
       for line in md_text.splitlines():
           line_stripped = line.rstrip()
           
           if line_stripped.startswith("```"):
               if in_code:
                   html.append("</code></pre>")
                   in_code = False
               else:
                   html.append("<pre><code>")
                   in_code = True
               continue
               
           if in_code:
               escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
               html.append(escaped)
               continue
               
           escaped = line_stripped.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
           
           if escaped.startswith("|") and escaped.endswith("|"):
               cells = [c.strip() for c in escaped.split("|")[1:-1]]
               if all(c.startswith("---") or c == "" for c in cells):
                   continue
               if not in_table:
                   html.append("<table>")
                   in_table = True
                   html.append("<thead><tr>")
                   for cell in cells:
                       html.append(f"<th>{cell}</th>")
                   html.append("</tr></thead><tbody>")
               else:
                   html.append("<tr>")
                   for cell in cells:
                       html.append(f"<td>{cell}</td>")
                   html.append("</tr>")
               continue
           else:
               if in_table:
                   html.append("</tbody></table>")
                   in_table = False
           
           if escaped.startswith("# "):
               html.append(f"<h1>{escaped[2:]}</h1>")
           elif escaped.startswith("## "):
               html.append(f"<h2>{escaped[3:]}</h2>")
           elif escaped.startswith("### "):
               html.append(f"<h3>{escaped[4:]}</h3>")
           elif escaped.startswith("#### "):
               html.append(f"<h4>{escaped[5:]}</h4>")
           elif escaped.startswith("- ") or escaped.startswith("* "):
               if not in_list:
                   html.append("<ul>")
                   in_list = True
               html.append(f"<li>{escaped[2:]}</li>")
           else:
               if in_list:
                   html.append("</ul>")
                   in_list = False
               if not escaped.strip():
                   html.append("<br/>")
               else:
                   html.append(f"<p>{escaped}</p>")
                   
       if in_list:
           html.append("</ul>")
       if in_code:
           html.append("</code></pre>")
       if in_table:
           html.append("</tbody></table>")
           
       result = "\\n".join(html)
       result = re.sub(r"\\*\\*(.*?)\\*\\*", r"<strong>\\1</strong>", result)
       result = re.sub(r"\\*(.*?)\\*", r"<em>\\1</em>", result)
       result = re.sub(r"`(.*?)`", r"<code>\\1</code>", result)
       result = re.sub(r"\\[(.*?)\\]\\((.*?)\\)", r'<a href="\\2" target="_blank">\\1</a>', result)
       
       return result

   with open("README.md", "r", encoding="utf-8") as f:
       content = f.read()

   html_body = md_to_html(content)

   template = f"""<!DOCTYPE html>
   <html>
   <head>
       <meta charset="UTF-8">
       <title>README</title>
       <link rel="preconnect" href="https://fonts.googleapis.com">
       <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
       <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
       <style>
           :root {{
               --bg-color: #0b0f19;
               --container-bg: #111827;
               --text-color: #e5e7eb;
               --text-muted: #9ca3af;
               --primary: #6366f1;
               --primary-hover: #818cf8;
               --border-color: #1f2937;
               --code-bg: #1f2937;
               --pre-bg: #0f172a;
               --inline-code-color: #ff7b72;
               --table-header-bg: #1f2937;
               --table-even-bg: #111827;
               --table-odd-bg: #151f32;
           }}
           
           body {{
               font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
               background: var(--bg-color);
               color: var(--text-color);
               padding: 40px 20px;
               line-height: 1.7;
               max-width: 850px;
               margin: auto;
           }}
           
           .markdown-body {{
               background: var(--container-bg);
               border: 1px solid var(--border-color);
               border-radius: 12px;
               padding: 40px;
               box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
           }}
           
           h1, h2, h3, h4 {{
               color: #ffffff;
               font-weight: 700;
               margin-top: 32px;
               margin-bottom: 16px;
               line-height: 1.3;
           }}
           
           h1 {{
               font-size: 2.25em;
               border-bottom: 2px solid var(--border-color);
               padding-bottom: 0.4em;
               margin-top: 0;
               background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 100%);
               -webkit-background-clip: text;
               -webkit-text-fill-color: transparent;
           }}
           
           h2 {{
               font-size: 1.6em;
               border-bottom: 1px solid var(--border-color);
               padding-bottom: 0.3em;
           }}
           
           h3 {{ font-size: 1.3em; }}
           h4 {{ font-size: 1.1em; }}
           
           p {{ margin-top: 0; margin-bottom: 20px; color: var(--text-color); }}
           
           ul {{ padding-left: 2em; margin-top: 0; margin-bottom: 20px; }}
           li {{ margin-top: 0.5em; }}
           
           pre {{
               background: var(--pre-bg);
               border: 1px solid var(--border-color);
               padding: 20px;
               border-radius: 8px;
               overflow: auto;
               font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace;
               font-size: 88%;
               line-height: 1.5;
               margin-bottom: 20px;
           }}
           
           code {{
               font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace;
               background: var(--code-bg);
               color: var(--inline-code-color);
               padding: 0.2em 0.4em;
               border-radius: 4px;
               font-size: 88%;
           }}
           
           pre code {{
               background: none;
               padding: 0;
               border-radius: 0;
               font-size: 100%;
               color: #f8fafc;
           }}
           
           a {{
               color: var(--primary);
               text-decoration: none;
               font-weight: 500;
               border-bottom: 1px dashed var(--primary);
               transition: all 0.2s ease;
           }}
           
           a:hover {{
               color: var(--primary-hover);
               border-bottom-style: solid;
           }}
           
           table {{
               border-spacing: 0;
               border-collapse: collapse;
               margin-top: 0;
               margin-bottom: 20px;
               width: 100%;
               border-radius: 8px;
               overflow: hidden;
               border: 1px solid var(--border-color);
           }}
           
           table th, table td {{
               padding: 10px 15px;
               border: 1px solid var(--border-color);
           }}
           
           table th {{
               background-color: var(--table-header-bg);
               font-weight: 600;
               text-align: left;
           }}
           
           table tr {{
               background-color: var(--table-odd-bg);
           }}
           
           table tr:nth-child(2n) {{
               background-color: var(--table-even-bg);
           }}
           
           pre::-webkit-scrollbar {{
               width: 8px;
               height: 8px;
           }}
           pre::-webkit-scrollbar-track {{
               background: var(--pre-bg);
           }}
           pre::-webkit-scrollbar-thumb {{
               background: var(--border-color);
               border-radius: 4px;
           }}
           pre::-webkit-scrollbar-thumb:hover {{
               background: var(--text-muted);
           }}
       </style>
   </head>
   <body>
   <div class="markdown-body">
   {html_body}
   </div>
   </body>
   </html>"""

   with open("readme.html", "w", encoding="utf-8") as f:
       f.write(template)
   '''
                   sh 'python3 generate_readme.py'
                   archiveArtifacts artifacts: 'readme.html', fingerprint: true
                   publishHTML([
                       allowMissing: false,
                       alwaysLinkToLastBuild: true,
                       keepAll: true,
                       reportDir: '.',
                       reportFiles: 'readme.html',
                       reportName: 'Project README'
                   ])
                   sh 'rm -f generate_readme.py readme.html'
               }
           }
       }
   }
   ```

# Output Contract

When writing or updating a `Jenkinsfile`, output:
1. **Target file path** of the `Jenkinsfile` (e.g. `sources/plugins/com.cdsoftware.recaptcha/Jenkinsfile`).
2. **Updated Jenkinsfile content** incorporating the standardized compile and README archiving stages.
