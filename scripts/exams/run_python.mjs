import { existsSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const args = process.argv.slice(2);

if (args.length === 0) {
  console.error("Usage: node scripts/exams/run_python.mjs <script.py> [...args]");
  process.exit(2);
}

const __filename = fileURLToPath(import.meta.url);
const repoRoot = resolve(dirname(__filename), "..", "..");
const bundledPython = join(
  dirname(dirname(dirname(process.execPath))),
  "python",
  process.platform === "win32" ? "python.exe" : "bin/python",
);
const codexBundledPython =
  process.platform === "win32" && process.env.USERPROFILE
    ? join(
        process.env.USERPROFILE,
        ".cache",
        "codex-runtimes",
        "codex-primary-runtime",
        "dependencies",
        "python",
        "python.exe",
      )
    : undefined;

const candidates = [
  process.env.PYTHON,
  bundledPython,
  codexBundledPython,
  process.platform === "win32" ? "python" : "python3",
  process.platform === "win32" ? "py" : undefined,
].filter(Boolean);

function canRun(command) {
  if (command.includes("\\") || command.includes("/")) {
    if (!existsSync(command)) {
      return false;
    }
  }
  const result = spawnSync(command, ["--version"], { encoding: "utf8", shell: false });
  return result.status === 0;
}

const python = candidates.find(canRun);

if (!python) {
  console.error("Unable to find Python. Set PYTHON to python.exe, or install Python on PATH.");
  process.exit(1);
}

const result = spawnSync(python, args, {
  cwd: repoRoot,
  env: process.env,
  encoding: "utf8",
  shell: false,
  stdio: "inherit",
});

process.exit(result.status ?? 1);
