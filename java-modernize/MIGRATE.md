## Java Upgrade Instructions

## Workflow
- Before starting an upgrade, check for an existing `.upgrade/upgrade_plan.json` file. If it exists, resume the upgrade from the first step with a 'pending' status. If it does not exist, create the `.upgrade/` directory and the `upgrade_plan.json` file.
- If a step is evaluated and no code changes are necessary, update the step's status to 'complete' in the `upgrade_plan.json` file, add a summary indicating that no changes were needed, and perform a git commit with the `--allow-empty` flag and a message like 'docs(upgrade): [Step X] No changes required for [file]' to record the evaluation.
- The git commit message MUST follow the format: `type(scope): [Step X] message`, where `X` is the step number. For example: `feat(catalog): [Step 3] Refactor CatalogRepository with Java 21 features`.
- If there is not a .upgrade/ folder, bbefore starting the upgrade create a folder inside the root folder called .upgrade/ Create a file called upgrade_plan.json in the .upgrade/ folder.
- Create a numbered step by step plan for how to upgrade this application. Add these steps to the upgrade_plan JSON file previously created. Make the steps discrete. For example, if individual files need to be upgraded, create separate steps for the individual files.
- The upgrade_plan JSON file should have each step and the prompt used to accomplish that step
- For each step, make the prompts descriptive, riche and more detailed so that the LLM can act upon it with ease and there are no chances for inaccurate responses
- Each step in the upgrade_plan JSON file should have a status and a git field. The git field should contain the git commit hash and the git commit message. The git commit message should contain the step number so its easy to correlate to the steps in the upgrade_plan.json file with the git commit messages.
- Each step should have a time field. Once the task is completed, update this field with the current time.
- IMPORTANT: Double check your work in the upgrade_plan.json file and make sure that the prompt are descriptive and detailed so that the LLMs can act upon them with ease and reeturn high quality responses.
- VERY IMPORTANT: After you have created the plan in the JSON file and BEFORE executing any of the steps, ask me for input, feedback and wait for me to give you a go ahead to execute the plan. Once I have given the green light, execute the plan step by step in order. Let me know which step you are executing.
- ALSO IMPORTANT: If the step is unsuccessful, try to resolve the error. 
- If you cannot resolve the error on your own, do a web search and try to find a reputable answer.
- If you still cannot resolve the error, STOP and ask me for help. 
- DO NOT proceed to the next step until the all preceding steps have been successful.
- Only proceed to the next step once the prior steps have been successfully completed.
- After each step is successfully completed, do a git commit and add a git commit message with the summary of the change (so that I have a commit history)
- After each step is successfully completed, update the status in the upgrade_plan JSON file.Only update the status in the upgrade_plan JSON file. Do not remove the prompt or any other information.
- For each completed step, create a summary field where give a summary of what changed during that step.
- After completing the plan, do NOT delete the upgrade_plan JSON  file.


### Upgrade instructions
- When upgrading this Java application, look in the `catalog/**` folder. Upgrade the `pom.xml` file first, upgrade all libraries and remove any deprecated libraries. Then go to the `catalog/**` folder and upgrade each file. Remove any old java syntax or libraries. Once all files are upgraded. Go to the `catalog/**` folder, use java 21 by running "sdk use java 21-tem" and then run maven springboot run to run the backend.
- My GitLab project ID is https://gitlab.com/duetailabs/cymbalbnb
- After completing the upgrade, commit all changes to the new branch in my GitLab project. In order to push to GitLab branch, you need to run the following command: "eval `ssh-agent` && ssh-add .ssh/gitlab_user && git push" and complete the command.
- Using the GitLab MCP server, Create a merge request from new branch into the "dev" branch in my GitLab project.


### Git
The git repo is in the root workspace folder.
Always create a new git branch before starting an upgrade. Name the branch upgrade/java21/date where date is in the format YY-MM-DD for example upgrade/java/25-06-25 (if the date is Jun 25th 2025). Check if the branch exists, otherwise create a new one.
Perform all upgrade steps in the new branch.

### Backend (Catalog Service)

The backend is a standard Maven project.

1.  **Navigate to the catalog directory:**
    ```bash
    cd catalog
    ```
2.  **Build the project using Maven:**
    ```bash
    ./mvnw springboot:run
    ```

