#!/usr/bin/env bash
set -euo pipefail

VERSION=$(python3 -c "
import tomllib
with open('pyproject.toml', 'rb') as f:
    print(tomllib.load(f)['project']['version'])
")
TAG="v${VERSION}"

echo "Version: ${TAG}"

# Check local tag
if git tag --list | grep -qx "${TAG}"; then
    echo "ERROR: local tag ${TAG} already exists" >&2
    exit 1
fi

# Check remote tag
if git ls-remote --tags origin | grep -q "refs/tags/${TAG}$"; then
    echo "ERROR: remote tag ${TAG} already exists" >&2
    exit 1
fi

# Check GitHub release
if gh release view "${TAG}" &>/dev/null; then
    echo "ERROR: GitHub release ${TAG} already exists" >&2
    exit 1
fi

echo "Creating tag ${TAG}..."
git tag -a "${TAG}" -m "${TAG}"

echo "Pushing tag..."
git push origin "${TAG}"

echo "Creating GitHub release..."
gh release create "${TAG}" --title "${TAG}" --generate-notes

echo "Done: ${TAG} released"
