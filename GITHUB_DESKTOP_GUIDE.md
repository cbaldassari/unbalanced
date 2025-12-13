# GitHub Desktop Guide - Connect to Existing Repository

## 🎯 Your Repository
**URL**: https://github.com/cbaldassari/unbalanced

You already created the repository on GitHub. Now we'll connect it with GitHub Desktop.

---

## 📦 PART 1: Download Repository

### Option A: Clone with GitHub Desktop (Recommended)

1. Open **GitHub Desktop**

2. Click **File** → **Clone Repository**

3. Click the **URL** tab

4. Enter:
   ```
   https://github.com/cbaldassari/unbalanced
   ```

5. Choose **Local Path** where you want to save it
   - Example: `C:\Users\YourName\Documents\GitHub\unbalanced`

6. Click **Clone**

⏳ Wait for download...

✅ **Done!** The repository is now on your computer.

---

## 📁 PART 2: Add Your Files

### Step 1: Copy Files to Repository

1. Open the repository folder (where GitHub Desktop cloned it)

2. Copy these folders/files from the downloaded zip:
   ```
   ✅ notebooks/     (all .ipynb files)
   ✅ data/          (logret_gas.dat, logret_electricity.dat)
   ✅ figures/       (folder for outputs)
   ✅ README.md      (documentation)
   ✅ requirements.txt
   ✅ .gitignore
   ✅ LICENSE
   ```

3. Paste them into your `unbalanced/` folder

### Step 2: Check in GitHub Desktop

Open GitHub Desktop - you'll see all new files in the **Changes** section.

---

## 💾 PART 3: First Commit

### Step 1: Review Changes

In GitHub Desktop, you'll see:
- ✅ All notebooks
- ✅ Data files
- ✅ Documentation

### Step 2: Commit

1. In the bottom-left corner, **Summary** field:
   ```
   Add paper implementation
   ```

2. In **Description** (optional):
   ```
   - Add 5 Jupyter notebooks (pipeline implementation)
   - Add real data (gas and electricity log-returns)
   - Add documentation and requirements
   ```

3. Click the blue **Commit to main** button

✅ **First commit done!**

---

## 📤 PART 4: Push to GitHub

### Push Your Changes

1. At the top, click **Push origin**

2. Wait a few seconds...

3. ✅ **Done!** Your files are now on GitHub!

### Verify Online

1. In GitHub Desktop, click **Repository** → **View on GitHub**

2. Your browser opens at: https://github.com/cbaldassari/unbalanced

3. You should see:
   - ✅ All folders (notebooks, data, figures)
   - ✅ README.md displayed nicely
   - ✅ All files uploaded

---

## ✏️ PART 5: Daily Workflow (Future Changes)

Every time you modify files:

### Step A: Make Changes
- Edit notebooks, add code, etc.
- Save files

### Step B: Commit in GitHub Desktop

1. Open GitHub Desktop
2. You'll see modified files in "Changes"
3. Write a descriptive commit message:
   ```
   Update preprocessing notebook
   ```
   or
   ```
   Add Wasserstein optimization
   ```
4. Click **Commit to main**

### Step C: Push to GitHub

1. Click **Push origin** (top right)
2. Changes are now online!

---

## 🎓 Common Commands

### View History
**View** → **History**: See all past commits

### Undo Last Commit
**Repository** → **Undo**: Undo last commit (if not pushed yet)

### Pull Changes
**Repository** → **Pull**: Download changes from GitHub
- Use if you work from multiple computers
- Or if you edited files directly on GitHub

### Create Branch (Advanced)
**Branch** → **New Branch**: Experiment without touching main

---

## 🆘 Troubleshooting

### "Changes" is empty
✅ Files already committed. All good!

### "Push origin" is greyed out
✅ No new commits to push. All good!

### Error during Push
1. Click **Repository** → **Pull**
2. Resolve any conflicts
3. Try Push again

### Can't see my changes online
1. Did you **Push**? (not just Commit)
2. Refresh the GitHub page

### Files too large (>100MB)
GitHub has a 100MB file limit. For large files:
- Don't commit data files >100MB
- Add them to `.gitignore`
- Provide download instructions instead

---

## 📋 Quick Checklist

**Initial Setup (Once):**
- [ ] Installed GitHub Desktop
- [ ] Logged into GitHub account
- [ ] Cloned repository from https://github.com/cbaldassari/unbalanced
- [ ] Copied all files to repository folder
- [ ] Made first commit
- [ ] Pushed to GitHub
- [ ] Verified files online

**For Each Change (Daily):**
- [ ] Made changes to files
- [ ] Opened GitHub Desktop
- [ ] Reviewed changes
- [ ] Written commit message
- [ ] Clicked "Commit to main"
- [ ] Clicked "Push origin"
- [ ] Verified changes online

---

## 🎯 Quick Summary

**First Time Setup:**
```
1. Open GitHub Desktop
2. File → Clone Repository
3. URL: https://github.com/cbaldassari/unbalanced
4. Copy your files into the cloned folder
5. Commit to main
6. Push origin
7. ✅ DONE!
```

**For Future Changes:**
```
1. Edit files
2. Open GitHub Desktop
3. Commit to main
4. Push origin
5. ✅ DONE!
```

---

## 💡 Tips

✅ **Commit often**: Many small commits > one big commit  
✅ **Clear messages**: "Add notebook 3" > "update"  
✅ **Push regularly**: Automatic cloud backup!  
✅ **Pull before editing**: If working from multiple computers  

---

## 📚 Additional Resources

- GitHub Desktop Documentation: [docs.github.com/desktop](https://docs.github.com/desktop)
- Your Repository: [github.com/cbaldassari/unbalanced](https://github.com/cbaldassari/unbalanced)

---

**Need Help?**  
Email: cristiano.baldassari@unitus.it
