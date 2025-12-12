# Website Deployment Guide

## Overview
Your website uses a Git submodule setup where:
- **Main repo**: `/Users/andreadepolis/Documents/My_Website` (source files)
- **Public submodule**: Points to `andreadepolis.github.io` (deployed site)
- **Docs folder**: Contains the built static site files

## Quick Deployment Steps

### Option A: Deploy from existing `docs` folder (Recommended)

```bash
# 1. Navigate to your website directory
cd "/Users/andreadepolis/Documents/My_Website"

# 2. Clear the public folder
rm -rf public/*

# 3. Copy docs content to public
cp -r docs/* public/

# 4. Navigate to public submodule
cd public

# 5. Stage all changes
git add .

# 6. Commit changes
git commit -m "Update website - [describe your changes]"

# 7. Push to GitHub Pages
git push origin main

# 8. Go back to parent directory
cd ..

# 9. Update the submodule reference in parent repo
git add public

# 10. Commit the submodule update
git commit -m "Update public submodule"

# 11. Push parent repo
git push origin master
```

**Done!** Your site will be live at https://andreadepolis.github.io in 1-2 minutes.

---

## Option B: Build with Hugo first (if you modified source files)

If you've made changes to content, config, or assets and need to rebuild:

```bash
# 1. Navigate to your website directory
cd "/Users/andreadepolis/Documents/My_Website"

# 2. Build the site with Hugo (generates to docs folder)
hugo -d docs

# 3. Follow steps 2-11 from Option A above
rm -rf public/*
cp -r docs/* public/
cd public
git add .
git commit -m "Update website - [describe your changes]"
git push origin main
cd ..
git add public
git commit -m "Update public submodule"
git push origin master
```

---

## Common Scenarios

### Scenario 1: Update content (e.g., add a new paper)

```bash
# 1. Edit your content files in /content directory
# 2. Rebuild with Hugo
hugo -d docs

# 3. Deploy (follow Option B steps 3-11)
```

### Scenario 2: Update existing HTML in docs folder

```bash
# 1. Edit files directly in /docs folder
# 2. Deploy (follow Option A steps 1-11)
```

### Scenario 3: Test locally before deploying

```bash
# Start a local server
cd "/Users/andreadepolis/Documents/My_Website"
python3 -m http.server 8000 --directory docs

# Open browser to: http://localhost:8000
# When satisfied, follow deployment steps above
```

---

## Troubleshooting

### Port already in use
```bash
# Kill existing Python servers
lsof -ti :8000 | xargs kill -9

# Or use a different port
python3 -m http.server 8080 --directory docs
```

### Submodule issues
```bash
# Reset submodule
git submodule update --init --recursive

# If public folder is out of sync
cd public
git checkout main
git pull origin main
cd ..
```

### Merge conflicts in public
```bash
cd public
git reset --hard origin/main
cd ..
# Then redeploy from scratch
```

### Force push (use with caution)
```bash
cd public
git push origin main --force
cd ..
```

---

## Repository Structure

```
My_Website/
├── docs/               # Built static site (source for deployment)
├── public/             # Git submodule → andreadepolis.github.io
├── content/            # Hugo content files
├── config/             # Hugo configuration
├── assets/             # Theme assets
├── static/             # Static files
└── DEPLOYMENT_GUIDE.md # This file
```

---

## Important Notes

1. **Always deploy from the `docs` folder** - this contains your working static site
2. **The `public` submodule** is what GitHub Pages actually serves
3. **Main branch** in public submodule = live website
4. **Master branch** in parent repo = source code
5. **Wait 1-2 minutes** after pushing for GitHub Pages to rebuild

---

## Backup Strategy

Before major changes:
```bash
# Create a backup branch
git checkout -b backup-YYYY-MM-DD
git add .
git commit -m "Backup before major changes"
git push origin backup-YYYY-MM-DD
git checkout master
```

---

## Quick Reference Commands

```bash
# Check git status
git status

# View current branch
git branch

# Check submodule status
git submodule status

# View remote URLs
git remote -v

# Check what's in public
cd public && git log --oneline -5 && cd ..
```

---

## Contact & Resources

- GitHub Repo: https://github.com/andreadepolis/andreadepolis.github.io
- Live Site: https://andreadepolis.github.io
- Hugo Docs: https://gohugo.io/documentation/

---

**Last Updated**: October 2025
