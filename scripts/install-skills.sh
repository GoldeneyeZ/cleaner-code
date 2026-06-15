#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "${SCRIPT_DIR}/.." && pwd)"
SOURCE_DIR="${REPO_ROOT}/cleaner-code-skillsets"
TARGET_DIR="${HOME}/.agents/skills"
INSTALL_NAME="cleaner-code-skillsets"
MODE="link"
DRY_RUN="false"

usage() {
  cat <<'USAGE'
Usage: scripts/install-skills.sh [options]

Installs this repository's cleaner-code-skillsets into ~/.agents/skills/cleaner-code-skillsets.

Options:
  --target DIR   Install into DIR instead of ~/.agents/skills
  --name NAME    Use NAME as the installed root name (default: cleaner-code-skillsets)
  --copy         Copy cleaner-code-skillsets into the target
  --link         Symlink target/NAME back to this repository (default)
  --dry-run      Print actions without changing files
  -h, --help     Show this help
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      if [ "$#" -lt 2 ]; then
        echo "error: --target requires a directory" >&2
        exit 2
      fi
      TARGET_DIR="$2"
      shift 2
      ;;
    --name)
      if [ "$#" -lt 2 ]; then
        echo "error: --name requires a value" >&2
        exit 2
      fi
      INSTALL_NAME="$2"
      shift 2
      ;;
    --copy)
      MODE="copy"
      shift
      ;;
    --link)
      MODE="link"
      shift
      ;;
    --dry-run)
      DRY_RUN="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "error: unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [ ! -d "${SOURCE_DIR}" ]; then
  echo "error: missing source directory: ${SOURCE_DIR}" >&2
  exit 1
fi

run() {
  if [ "${DRY_RUN}" = "true" ]; then
    printf '+'
    printf ' %q' "$@"
    printf '\n'
  else
    "$@"
  fi
}

install_copy() {
  local destination="${TARGET_DIR}/${INSTALL_NAME}"

  if [ -L "${destination}" ]; then
    echo "error: ${destination} is a symlink; use --link or remove it first" >&2
    exit 1
  fi

  run mkdir -p "${destination}"
  run cp -a "${SOURCE_DIR}/." "${destination}/"
  echo "Installed skills into ${destination}"
}

install_link() {
  local destination="${TARGET_DIR}/${INSTALL_NAME}"

  run mkdir -p "${TARGET_DIR}"

  if [ -e "${destination}" ] || [ -L "${destination}" ]; then
    if [ -L "${destination}" ] && [ "$(readlink "${destination}")" = "${SOURCE_DIR}" ]; then
      echo "cleaner-code-skillsets already linked at ${destination}"
      return
    fi

    echo "error: ${destination} already exists; remove it first or use --copy" >&2
    exit 1
  fi

  run ln -s "${SOURCE_DIR}" "${destination}"
  echo "Linked skills at ${destination} -> ${SOURCE_DIR}"
}

case "${MODE}" in
  copy)
    install_copy
    ;;
  link)
    install_link
    ;;
  *)
    echo "error: invalid mode: ${MODE}" >&2
    exit 2
    ;;
esac
