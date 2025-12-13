# GitHub Desktop - Drag & Drop Guide

## 🎯 Your Repository
**URL**: https://github.com/cbaldassari/unbalanced  
**Status**: Already created and empty

---

## 📦 STEP 1: Clone Repository (One Time)

### Open GitHub Desktop

1. Open **GitHub Desktop** application

2. Click **File** → **Clone Repository**

3. You should see `cbaldassari/unbalanced` in the list
   - If YES: Click on it → Click **Clone**
   - If NO: Click **URL** tab and enter:
     ```
     https://github.com/cbaldassari/unbalanced
     ```

4. Choose where to save it on your computer
   - Example: `C:\Users\YourName\Documents\GitHub\unbalanced`
   - Or: `~/Documents/GitHub/unbalanced` (Mac/Linux)

5. Click **Clone**

⏳ Wait a moment...

✅ **Done!** The repository is now on your computer.

**Remember this location!** You'll drag files here.

---

## 📂 STEP 2: Extract Your ZIP

1. Find your downloaded ZIP file (the one with all the files)

2. **Right-click** on the ZIP → **Extract All** (Windows)
   - Or double-click (Mac)

3. You'll get a folder with:
   ```
   ├── notebooks/
   ├── data/
   ├── figures/
   ├── README.md
   ├── requirements.txt
   ├── etc.
   ```

---

## 🎯 STEP 3: Drag & Drop (The Easy Part!)

### Open Two Windows Side by Side

**Window 1**: The extracted folder (where you unzipped)

**Window 2**: The cloned repository folder
- This is where GitHub Desktop cloned it
- Example: `C:\Users\YourName\Documents\GitHub\unbalanced`

### Drag Everything

1. **Select ALL** files and folders from Window 1:
   - `notebooks/` folder
   - `data/` folder
   - `figures/` folder
   - `README.md`
   - `requirements.txt`
   - `.gitignore`
   - `LICENSE`
   - `GITHUB_DESKTOP_GUIDE.md`
   - Everything!

2. **Drag** them all into Window 2 (the repository folder)

3. **Drop** them there

4. If asked "Replace files?", click **Yes** or **Replace All**

✅ **Done!** All files are now in your repository.

---

## 💾 STEP 4: Commit in GitHub Desktop

1. **Open GitHub Desktop**

2. You'll see ALL the new files in the **Changes** section (left side)

3. Look at the bottom-left corner:

   **Summary** field (required):
   ```
   Add paper implementation
   ```

   **Description** field (optional):
   ```
   - Add 5 Jupyter notebooks
   - Add real data (1825 observations)
   - Add documentation
   ```

4. Click the big blue button: **Commit to main**

✅ **Committed!** Files are ready to upload.

---

## 📤 STEP 5: Push to GitHub

1. At the top of GitHub Desktop, click **Push origin**

2. Wait a few seconds... (you'll see a progress bar)

3. ✅ **Done!** Files are now on GitHub!

---

## ✅ STEP 6: Verify Online

1. In GitHub Desktop, click **Repository** → **View on GitHub**

   OR

   Open browser and go to: https://github.com/cbaldassari/unbalanced

2. You should see:
   - ✅ `notebooks/` folder
   - ✅ `data/` folder
   - ✅ `figures/` folder
   - ✅ `README.md` displayed nicely
   - ✅ All files uploaded

3. Click on `notebooks/` → You should see all 5 `.ipynb` files

4. Click on `data/` → You should see the data files

✅ **Perfect!** Everything is online!

---

## 🎉 That's It!

You just uploaded your entire repository with drag & drop!

**Summary of what you did:**
1. ✅ Cloned empty repository
2. ✅ Extracted ZIP
3. ✅ Dragged & dropped all files
4. ✅ Committed
5. ✅ Pushed
6. ✅ Verified online

**Total time**: ~5 minutes!

---

## 🔄 Future Changes (Even Easier!)

When you edit files later:

1. **Edit** your files (notebooks, code, etc.)
2. **Save** them
3. **Open GitHub Desktop**
4. **Write** commit message
5. **Commit to main**
6. **Push origin**

Done! 🎯

---

## 📝 Visual Guide

```
Your Computer                          GitHub Desktop                  GitHub.com
─────────────                          ──────────────                  ──────────

1. [ZIP file]
      ↓ Extract
2. [Extracted folder]
      ↓ Drag & Drop
3. [Repository folder] ────────────→  Shows changes
                                            ↓ Commit
4.                                     Committed locally
                                            ↓ Push
5.                                                            Files online! ✅
```

---

## 🆘 Common Issues

### I don't see my repository in GitHub Desktop

**Solution**: 
1. Click **File** → **Clone Repository**
2. Click **URL** tab
3. Enter: `https://github.com/cbaldassari/unbalanced`
4. Clone

### Drag & drop didn't work

**Solution**: Just copy-paste instead:
1. Select all files in extracted folder
2. **Ctrl+C** (or Cmd+C on Mac)
3. Go to repository folder
4. **Ctrl+V** (or Cmd+V on Mac)

### GitHub Desktop doesn't show changes

**Solution**: 
1. Make sure you dragged files to the RIGHT folder (the cloned one)
2. Click **Repository** → **Refresh** in GitHub Desktop

### Push failed

**Solution**:
1. Click **Repository** → **Pull** first
2. Then try **Push** again

### Files are too large (>100MB)

**Solution**: 
- GitHub has 100MB file limit
- If you have large files, don't include them
- Add them to `.gitignore` instead

---

## ✅ Checklist

- [ ] GitHub Desktop installed and logged in
- [ ] Repository cloned: `cbaldassari/unbalanced`
- [ ] ZIP extracted
- [ ] All files dragged & dropped to repository folder
- [ ] Changes appear in GitHub Desktop
- [ ] Commit message written
- [ ] Clicked "Commit to main"
- [ ] Clicked "Push origin"
- [ ] Verified files online at github.com/cbaldassari/unbalanced

---

## 💡 Pro Tips

✅ **Organize**: Keep repository folder organized (don't move it after cloning)

✅ **Check first**: Before drag & drop, verify you have the right folder

✅ **Commit often**: Small, frequent commits are better than one huge commit

✅ **Meaningful messages**: "Add preprocessing" is better than "update"

---

**Need help?**  
- GitHub Desktop docs: [docs.github.com/desktop](https://docs.github.com/desktop)
- Email: cristiano.baldassari@unitus.it

---

**That's it!** Simple drag & drop, commit, push. Done! 🎉
