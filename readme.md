# 🎯 TO-DO LIST CLI - COMPLETE ASSIGNMENT GUIDE
## Jenkins Automated CI/CD Pipeline

**For Students with Roll Number % 2 = 1**

---

## 📋 ASSIGNMENT REQUIREMENTS

✅ Pull code from GitHub  
✅ Build the code  
✅ Test the code  
✅ Create Docker image (if tests pass)  
✅ Push to Docker Hub under your roll number  

---

## 🚀 STEP-BY-STEP SETUP

### **STEP 1: Create New GitHub Repository**

1. Go to https://github.com
2. Click "New Repository"
   - Repository name: `todo-cli-app`
   - Description: "To-Do List CLI Application with Jenkins CI/CD"
   - Visibility: **Public**
   - ✅ Initialize with README
3. Click "Create Repository"

---

### **STEP 2: Setup Project Files Locally**

```bash
# Create project directory
mkdir todo-cli-app
cd todo-cli-app

# Initialize git
git init
git remote add origin https://github.com/YOUR_USERNAME/todo-cli-app.git
```

---

### **STEP 3: Add Project Files**

Copy these 4 files to your `todo-cli-app` directory:

1. ✅ `todo.py` (Main application)
2. ✅ `test_todo.py` (Test file)
3. ✅ `Dockerfile` (Docker configuration)
4. ✅ `Jenkinsfile` (Jenkins pipeline)

**File names must be EXACTLY as shown above!**

---

### **STEP 4: Update Jenkinsfile**

Open `Jenkinsfile` and update line 7:

```groovy
ROLL_NUMBER = 'YOUR_ROLL_NUMBER'  // Replace with YOUR actual roll number
```

**Example:**
```groovy
ROLL_NUMBER = '2023001'  // If your roll number is 2023001
```

---

### **STEP 5: Push to GitHub**

```bash
# Add all files
git add .

# Commit
git commit -m "Initial commit: To-Do List CLI with Jenkins pipeline"

# Push to GitHub
git branch -M main
git push -u origin main
```

---

### **STEP 6: Verify GitHub Repository**

Go to your GitHub repository and verify you see:
- ✅ todo.py
- ✅ test_todo.py
- ✅ Dockerfile
- ✅ Jenkinsfile
- ✅ README.md (optional)

---

### **STEP 7: Configure Jenkins Credentials**

**(You already have these from earlier setup!)**

**GitHub Credentials:**
- ID: `github-creds`
- Username: Your GitHub username
- Password: Your GitHub Personal Access Token

**Docker Hub Credentials:**
- ID: `docker-hub-credentials`
- Username: `saivenkat1507`
- Password: `[Your Docker Hub Personal Access Token]`

---

### **STEP 8: Create Jenkins Pipeline**

1. **Jenkins Dashboard** → **New Item**
2. **Item name:** `TODO-CLI-Pipeline`
3. **Type:** Pipeline
4. Click **OK**

**Configure Pipeline:**

```
Description: "To-Do List CLI Application - Automated Pipeline"

✅ GitHub project
   Project URL: https://github.com/YOUR_USERNAME/todo-cli-app

✅ Build Triggers
   ☑ GitHub hook trigger for GITScm polling (optional)

Pipeline:
   Definition: Pipeline script from SCM
   SCM: Git
   Repository URL: https://github.com/YOUR_USERNAME/todo-cli-app.git
   Credentials: github-creds
   Branch Specifier: */main
   Script Path: Jenkinsfile
```

5. Click **Save**

---

### **STEP 9: Make Sure Docker Desktop is Running**

```bash
# On Mac
open -a Docker

# Wait 30 seconds, then verify
docker ps
```

---

### **STEP 10: Run the Pipeline**

1. Go to your Jenkins job: **TODO-CLI-Pipeline**
2. Click **"Build Now"**
3. Watch the build in "Build History"

**Expected Stages:**
1. ✅ Pull Code from GitHub
2. ✅ Build Code
3. ✅ Test Code
4. ✅ Create Docker Image
5. ✅ Push to Docker Hub

---

### **STEP 11: Verify Docker Image**

**In Terminal:**
```bash
# Check local images
docker images | grep todo-cli

# You should see:
# saivenkat1507/todo-cli   latest   abc123   2 minutes ago   150MB
```

**On Docker Hub:**
1. Go to https://hub.docker.com/
2. Login
3. Check "Repositories"
4. You should see: `todo-cli`

---

### **STEP 12: Capture Screenshots**

#### **Screenshot 1: Pipeline Stage View**
1. Click on your successful build (e.g., #1)
2. View showing all 5 stages with ✅ green checkmarks
3. Save as: `jenkins_pipeline_stages.png`

#### **Screenshot 2: Console Output**
1. Same build → Click "Console Output"
2. Scroll to show:
   - "Pulling code from GitHub"
   - "Running tests"
   - "All tests passed"
   - "Docker image created"
   - "PIPELINE COMPLETED SUCCESSFULLY!"
3. Save as: `jenkins_console_output.png`

---

### **STEP 13: Test Your Docker Image**

```bash
# Pull from Docker Hub
docker pull saivenkat1507/todo-cli:latest

# Run the application
docker run -it saivenkat1507/todo-cli:latest

# You should see the To-Do List menu!
```

---

## 📦 WHAT TO SUBMIT

### 1. **GitHub Repository Link**
```
https://github.com/YOUR_USERNAME/todo-cli-app
```

### 2. **Screenshots** (2 files)
- `jenkins_pipeline_stages.png` - All stages showing ✅
- `jenkins_console_output.png` - Console showing success

### 3. **Docker Hub Link**
```
https://hub.docker.com/r/saivenkat1507/todo-cli
```

### 4. **Submission Document** (Create a simple text file)

```
JENKINS CI/CD PIPELINE ASSIGNMENT
Student Name: [Your Name]
Roll Number: [Your Roll Number]

Application: To-Do List CLI (Roll % 2 = 1)

GitHub Repository:
https://github.com/YOUR_USERNAME/todo-cli-app

Docker Hub Image:
https://hub.docker.com/r/saivenkat1507/todo-cli

Jenkins Pipeline:
- 5 Stages completed successfully
- All tests passed
- Docker image created and pushed

Pull Command:
docker pull saivenkat1507/todo-cli:latest

Run Command:
docker run -it saivenkat1507/todo-cli:latest

Screenshots attached:
1. jenkins_pipeline_stages.png
2. jenkins_console_output.png
```

---

## 🔍 VERIFY EVERYTHING WORKS

### Test the application locally:
```bash
# Run Python app directly
python3 todo.py

# Run tests
python3 test_todo.py

# Build Docker image locally
docker build -t todo-test .

# Run Docker container
docker run -it todo-test
```

---

## ⚠️ TROUBLESHOOTING

### Problem 1: "docker: command not found" in Jenkins
**Solution:** Make sure Docker Desktop is running
```bash
open -a Docker
# Wait 30 seconds, then rebuild in Jenkins
```

### Problem 2: Tests fail
**Solution:** Check test output
```bash
python3 test_todo.py
# Fix any errors shown
```

### Problem 3: GitHub authentication fails
**Solution:** Regenerate GitHub Personal Access Token
- GitHub → Settings → Developer settings → Personal access tokens
- Generate new token with `repo` scope
- Update credentials in Jenkins

### Problem 4: Docker push fails
**Solution:** Verify Docker Hub credentials
```bash
docker login
# Username: saivenkat1507
# Password: [Use your Docker Hub Personal Access Token]
```

---

## ✅ FINAL CHECKLIST

Before submission, verify:

- [ ] GitHub repository is public and contains all 4 files
- [ ] Jenkinsfile has your roll number updated
- [ ] Jenkins pipeline runs successfully (all stages green)
- [ ] Docker image appears in `docker images`
- [ ] Docker image is on Docker Hub
- [ ] Screenshot 1: Pipeline stages (all green ✅)
- [ ] Screenshot 2: Console output (shows success)
- [ ] You can pull and run from Docker Hub

---

## 🎉 SUCCESS CRITERIA

Your assignment is complete when:

✅ Jenkins pipeline runs successfully  
✅ All 5 stages pass (Pull → Build → Test → Docker → Push)  
✅ Tests pass (10/10 tests successful)  
✅ Docker image created (`docker images` shows it)  
✅ Docker image on Docker Hub  
✅ Screenshots captured  
✅ Application runs from Docker image  

---

## 📞 QUICK REFERENCE

**Your Project:**
- App: To-Do List CLI
- GitHub: `https://github.com/YOUR_USERNAME/todo-cli-app`
- Docker Hub: `saivenkat1507/todo-cli`
- Jenkins Job: `TODO-CLI-Pipeline`

**Important Commands:**
```bash
# Build locally
docker build -t saivenkat1507/todo-cli:latest .

# Run locally
docker run -it saivenkat1507/todo-cli:latest

# Push to Docker Hub
docker push saivenkat1507/todo-cli:latest

# Pull from Docker Hub
docker pull saivenkat1507/todo-cli:latest
```

---

**Good luck! 🚀**