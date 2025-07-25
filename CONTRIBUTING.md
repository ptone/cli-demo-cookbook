# How to Contribute

We'd love to accept your patches and contributions to this project. There are
just a few small guidelines you need to follow.

Each demo is self-contained in its own folder. The demo should consist of:

 - Any code or files that are part of the demo setup. This may be some existing code sample to work on, context files, data files, etc.
 - A processed [asciinema](https://asciinema.org/) recording of the demo (recommended, see additional instructions below) (.cast file)
 - A demo specific readme that describes any setup, key prompts used, steps the CLI takes, and features and capabilities demonstrated. (Gemini can help with this see additional technical directions below)

 ## Demo Categories

 Demos will generally fit into one of several types, this is an evolving taxonomy

  - Features and how to use Gemini CLI, a deeper dive and run through of what might be covered in doucmentation, but not always discovered as easily.
  - Code and software Generation use-cases
  - Non code-centric use-cases
  - Best practices
  - Advanced, experimental, or frontier usage (pushing the boundaries)

## Technical Directions

- Install Gemini CLI
- Install [asciinema](https://asciinema.org/)
- Create a fork of the repo and branch for your demo
- Create a subfolder for your demo - if it is language or framework centric, use that as as prefix
- Set up the "before" context of your demo, this is what will be committed.
  - tip: folders named "demo-meta" are in this project's gitignore, if you want to preserve a copy of your before state there while you test or re-record demo, that can be handy.
- Use the following command to start asciinema
  - `asciinema rec -i .75 --overwrite -t "Gemini CLI Demo" --cols 100 --rows 30 -c gemini demo-orig.cast`
  - This assumes you have Gemini CLI on your path
  - record your demo flow, note that the -i .75 will shorten any idle time to .75 seconds, so don't feel you need to rush every step, this is not a video recording
- Before exiting the demo recording, finish with `/chat save demo` in the CLI, this will save a "transcript" of your demo session.
- Post-process your cast recording with the following (assumes you have system python3 installed)
  - `python3 ../tools/retime.py demo-orig.cast 3 > demo.cast`
  - This will apply a 3x speed up to the "thinking time" of the model steps, providing for a faster demo. This should be disclosed by anyone re-playing the demo, and is self-evident in the 'seconds' display of the thinking status.
- Generate an initial readme for this demo with the following command (run from your demo folder)
  - `(echo "Write a brief summary of what this demo does to a new ./README.md file local to this directory, including key initial and followup prompts, the features and capabilities demonstrated, and a review of steps taken by the Gemini CLI based on the transcript: "; cat "$(node ../tools/gemini-hash-dir.mjs)") | gemini -y`
  - Review and adjust this readme before committing
- Submit a pull request to include your demo
 

## Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License
Agreement (CLA). You (or your employer) retain the copyright to your
contribution; this simply gives us permission to use and redistribute your
contributions as part of the project. Head over to
<https://cla.developers.google.com/> to see your current agreements on file or
to sign a new one.

You generally only need to submit a CLA once, so if you've already submitted one
(even if it was for a different project), you probably don't need to do it
again.

## Code Reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.

## Community Guidelines

This project follows
[Google's Open Source Community Guidelines](https://opensource.google/conduct/).