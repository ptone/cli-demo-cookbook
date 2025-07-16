import crypto from 'crypto';
import path from 'path';
import os from 'os';

// Get the absolute path for the current working directory.
const projectRoot = path.resolve(process.cwd());

// Generate a SHA256 hash of the project root path, which is how Gemini CLI
// creates a unique ID for a workspace.
const hash = crypto.createHash('sha256').update(projectRoot).digest('hex');

const geminiPath = path.join(os.homedir(), '.gemini', 'tmp', hash, 'checkpoint-demo.json');

console.log(geminiPath);