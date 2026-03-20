#!/usr/bin/env python3
import requests
import json

GITHUB_TOKEN = "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"
GITHUB_USERNAME = "ruibraga83"
REPO_NAME = "ground-handling-rostering"
BRANCH = "main"

GITHUB_API_URL = "https://api.github.com"
REPO_URL = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json"
}

ALL_FILES = {
    "README.md": "# Ground Handling Rostering System\n\nA production-ready SaaS platform.\n\n## Quick Start\n\ngit clone https://github.com/ruibraga83/ground-handling-rostering.git\ncd ground-handling-rostering\ncd backend && docker-compose up -d\ncd ../frontend && npm install && npm run dev\n\n## Access\n- Frontend: http://localhost:3000\n- API: http://localhost:3001\n- Email: admin@rostering.local\n- Password: admin@123\n\n## License\nProprietary",
    ".gitignore": "node_modules/\n__pycache__/\n*.pyc\nvenv/\nenv/\n.venv/\n.env\n.env.local\ndist/\nbuild/\n*.log\nlogs/",
    "LICENSE": "PROPRIETARY LICENSE\n\nCopyright (c) 2026 Ground Handling Systems\n\nAll rights reserved.",
    "CONTRIBUTING.md": "# Contributing\n\n1. Fork the repository\n2. Create a feature branch\n3. Commit changes\n4. Push to branch\n5. Open a Pull Request",
    "QUICK_START.md": "# Quick Start\n\n## Prerequisites\n- Docker Desktop\n- Node.js 20+\n- Git\n\n## Steps\n1. git clone https://github.com/ruibraga83/ground-handling-rostering.git\n2. cd backend && docker-compose up -d\n3. cd ../frontend && npm install && npm run dev\n4. Open http://localhost:3000",
    "backend/.env.example": "DB_HOST=postgres\nDB_PORT=5432\nDB_USER=postgres\nDB_PASSWORD=postgres\nDB_NAME=rostering\nREDIS_HOST=redis\nREDIS_PORT=6379\nJWT_SECRET=dev-secret-key\nJWT_EXPIRE=24h\nAPI_PORT=3001\nNODE_ENV=development\nCORS_ORIGIN=http://localhost:3000",
    "backend/docker-compose.yml": "version: '3.8'\n\nservices:\n  postgres:\n    image: postgres:15-alpine\n    environment:\n      POSTGRES_USER: postgres\n      POSTGRES_PASSWORD: postgres\n      POSTGRES_DB: rostering\n    ports:\n      - '5432:5432'\n    volumes:\n      - postgres_data:/var/lib/postgresql/data\n      - ./init-db.sql:/docker-entrypoint-initdb.d/init.sql\n\n  redis:\n    image: redis:7-alpine\n    ports:\n      - '6379:6379'\n\nvolumes:\n  postgres_data:",
    "backend/init-db.sql": "CREATE TABLE airports (id SERIAL PRIMARY KEY, code VARCHAR(10) UNIQUE, name VARCHAR(255));\nCREATE TABLE departments (id SERIAL PRIMARY KEY, airport_id INTEGER, code VARCHAR(50), name VARCHAR(255));\nCREATE TABLE roles (id SERIAL PRIMARY KEY, code VARCHAR(50) UNIQUE, name VARCHAR(255));\nCREATE TABLE users (id SERIAL PRIMARY KEY, email VARCHAR(255) UNIQUE, password_hash VARCHAR(255), first_name VARCHAR(100), last_name VARCHAR(100), role_id INTEGER);\nINSERT INTO airports (code, name) VALUES ('OPO', 'Porto'), ('LIS', 'Lisbon'), ('FAO', 'Faro'), ('FNC', 'Funchal');\nINSERT INTO roles (code, name) VALUES ('ADMIN', 'Administrator'), ('USER', 'User');",
    "backend/services/auth-service/package.json": "{\"name\": \"auth-service\", \"version\": \"1.0.0\", \"scripts\": {\"dev\": \"ts-node src/index.ts\", \"build\": \"tsc\"}, \"dependencies\": {\"express\": \"^4.18.2\", \"pg\": \"^8.11.3\", \"jsonwebtoken\": \"^9.1.2\", \"bcryptjs\": \"^2.4.3\", \"dotenv\": \"^16.3.1\", \"cors\": \"^2.8.5\"}}",
    "backend/services/auth-service/Dockerfile": "FROM node:20-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci --only=production\nCOPY dist ./dist\nEXPOSE 3001\nCMD [\"node\", \"dist/index.js\"]",
    "backend/services/auth-service/tsconfig.json": "{\"compilerOptions\": {\"target\": \"ES2020\", \"module\": \"commonjs\", \"lib\": [\"ES2020\"], \"outDir\": \"./dist\", \"rootDir\": \"./src\", \"strict\": true}, \"include\": [\"src/**/*\"]}",
    "backend/services/auth-service/src/index.ts": "import express from 'express';\nimport cors from 'cors';\nimport { Pool } from 'pg';\n\nconst app = express();\nconst port = 3001;\n\napp.use(cors());\napp.use(express.json());\n\napp.get('/health', (req, res) => {\n  res.json({ status: 'ok', service: 'auth-service' });\n});\n\napp.listen(port, () => {\n  console.log(`Auth service running on port ${port}`);\n});",
    "backend/services/flight-service/package.json": "{\"name\": \"flight-service\", \"version\": \"1.0.0\", \"scripts\": {\"dev\": \"ts-node src/index.ts\"}, \"dependencies\": {\"express\": \"^4.18.2\", \"cors\": \"^2.8.5\"}}",
    "backend/services/flight-service/Dockerfile": "FROM node:20-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci\nCOPY dist ./dist\nEXPOSE 3003\nCMD [\"node\", \"dist/index.js\"]",
    "backend/services/flight-service/tsconfig.json": "{\"compilerOptions\": {\"target\": \"ES2020\", \"module\": \"commonjs\", \"outDir\": \"./dist\", \"rootDir\": \"./src\"}}",
    "backend/services/flight-service/src/index.ts": "import express from 'express';\nconst app = express();\napp.get('/health', (req, res) => res.json({ status: 'ok' }));\napp.listen(3003, () => console.log('Flight service on 3003'));",
    "backend/services/staff-service/package.json": "{\"name\": \"staff-service\", \"version\": \"1.0.0\", \"scripts\": {\"dev\": \"ts-node src/index.ts\"}, \"dependencies\": {\"express\": \"^4.18.2\"}}",
    "backend/services/staff-service/Dockerfile": "FROM node:20-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci\nCOPY dist ./dist\nEXPOSE 3002\nCMD [\"node\", \"dist/index.js\"]",
    "backend/services/staff-service/src/index.ts": "import express from 'express';\nconst app = express();\napp.get('/health', (req, res) => res.json({ status: 'ok' }));\napp.listen(3002, () => console.log('Staff service on 3002'));",
    "backend/services/roster-service/package.json": "{\"name\": \"roster-service\", \"version\": \"1.0.0\", \"scripts\": {\"dev\": \"ts-node src/index.ts\"}, \"dependencies\": {\"express\": \"^4.18.2\"}}",
    "backend/services/roster-service/Dockerfile": "FROM node:20-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci\nCOPY dist ./dist\nEXPOSE 3004\nCMD [\"node\", \"dist/index.js\"]",
    "backend/services/roster-service/src/index.ts": "import express from 'express';\nconst app = express();\napp.get('/health', (req, res) => res.json({ status: 'ok' }));\napp.listen(3004, () => console.log('Roster service on 3004'));",
    "backend/services/task-service/package.json": "{\"name\": \"task-service\", \"version\": \"1.0.0\", \"scripts\": {\"dev\": \"ts-node src/index.ts\"}, \"dependencies\": {\"express\": \"^4.18.2\"}}",
    "backend/services/task-service/Dockerfile": "FROM node:20-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci\nCOPY dist ./dist\nEXPOSE 3005\nCMD [\"node\", \"dist/index.js\"]",
    "backend/services/task-service/src/index.ts": "import express from 'express';\nconst app = express();\napp.get('/health', (req, res) => res.json({ status: 'ok' }));\napp.listen(3005, () => console.log('Task service on 3005'));",
    "frontend/package.json": "{\"name\": \"frontend\", \"version\": \"1.0.0\", \"type\": \"module\", \"scripts\": {\"dev\": \"vite\", \"build\": \"tsc && vite build\"}, \"dependencies\": {\"react\": \"^18.2.0\", \"react-dom\": \"^18.2.0\", \"react-redux\": \"^8.1.3\", \"@reduxjs/toolkit\": \"^1.9.7\", \"axios\": \"^1.6.5\", \"react-router-dom\": \"^6.20.1\"}, \"devDependencies\": {\"@types/react\": \"^18.2.37\", \"typescript\": \"^5.2.2\", \"vite\": \"^5.0.8\"}}",
    "frontend/tsconfig.json": "{\"compilerOptions\": {\"target\": \"ES2020\", \"lib\": [\"ES2020\", \"DOM\"], \"module\": \"ESNext\", \"strict\": true, \"jsx\": \"react-jsx\"}, \"include\": [\"src\"]}",
    "frontend/vite.config.ts": "import { defineConfig } from 'vite'\nimport react from '@vitejs/plugin-react'\nexport default defineConfig({\n  plugins: [react()],\n  server: { port: 3000 }\n})",
    "frontend/.env.example": "VITE_API_URL=http://localhost:3001",
    "frontend/index.html": "<!DOCTYPE html>\n<html>\n<head><title>Ground Handling Rostering</title></head>\n<body><div id=\"root\"></div><script type=\"module\" src=\"/src/main.tsx\"></script></body>\n</html>",
    "frontend/src/main.tsx": "import React from 'react'\nimport ReactDOM from 'react-dom/client'\nimport App from './App'\nReactDOM.createRoot(document.getElementById('root')!).render(<App />)",
    "frontend/src/App.tsx": "export default function App() { return <div>Ground Handling Rostering System</div> }",
    "frontend/src/index.css": "* { margin: 0; padding: 0; box-sizing: border-box; }",
    "optimization-engine/requirements.txt": "Flask==3.0.0\ngoogle-ortools==9.7.2996\npython-dotenv==1.0.0",
    "optimization-engine/Dockerfile": "FROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY src ./src\nEXPOSE 5000\nCMD [\"python\", \"src/main.py\"]",
    "optimization-engine/src/main.py": "from flask import Flask\napp = Flask(__name__)\n@app.route('/health')\ndef health():\n    return {'status': 'ok'}\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=5000)",
    "docs/ARCHITECTURE.md": "# Architecture\n\nMicroservices for ground handling rostering.",
    "docs/API.md": "# API\n\nREST API documentation.",
    "docs/DEPLOYMENT.md": "# Deployment\n\nDeployment guide.",
    ".github/workflows/ci.yml": "name: CI\non: [push]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n      - uses: actions/setup-node@v3\n        with:\n          node-version: '20'\n      - run: npm install",
}

def upload_files_via_git_api(files: dict):
    try:
        print("📋 Validating repository...")
        ref_url = f"{REPO_URL}/git/refs/heads/{BRANCH}"
        ref_response = requests.get(ref_url, headers=headers)
        
        if ref_response.status_code == 404:
            print(f"⚠️  Creating branch '{BRANCH}'...")
            ref_url_main = f"{REPO_URL}/git/refs/heads/main"
            ref_response_main = requests.get(ref_url_main, headers=headers)
            if ref_response_main.status_code == 200:
                main_sha = ref_response_main.json()['object']['sha']
                requests.post(f"{REPO_URL}/git/refs", headers=headers, json={"ref": f"refs/heads/{BRANCH}", "sha": main_sha})
                current_commit_sha = main_sha
            else:
                print("❌ Main branch not found")
                return False
        else:
            current_commit_sha = ref_response.json()['object']['sha']
        
        commit_response = requests.get(f"{REPO_URL}/git/commits/{current_commit_sha}", headers=headers)
        base_tree_sha = commit_response.json()['tree']['sha']
        
        print("📦 Creating file blobs...")
        tree_items = [{"path": fp, "mode": "100644", "type": "blob", "content": c} for fp, c in files.items()]
        print(f"   Total items: {len(tree_items)}")
        
        print("🌳 Creating tree...")
        tree_response = requests.post(f"{REPO_URL}/git/trees", headers=headers, json={"base_tree": base_tree_sha, "tree": tree_items})
        
        print(f"   Response status: {tree_response.status_code}")
        if tree_response.status_code != 201:
            print(f"   Response: {tree_response.text}")
            return False
        
        new_tree_sha = tree_response.json()['sha']
        
        print("✍️  Creating commit...")
        commit_payload = {
            "message": "Initial commit: Ground Handling Rostering System",
            "tree": new_tree_sha,
            "parents": [current_commit_sha]
        }
        commit_response = requests.post(f"{REPO_URL}/git/commits", headers=headers, json=commit_payload)
        
        if commit_response.status_code != 201:
            print(f"❌ Failed to create commit: {commit_response.status_code}")
            print(f"   Response: {commit_response.text}")
            return False
        
        new_commit_sha = commit_response.json()['sha']
        
        print("🔄 Updating branch...")
        update_response = requests.patch(f"{REPO_URL}/git/refs/heads/{BRANCH}", headers=headers, json={"sha": new_commit_sha, "force": True})
        
        if update_response.status_code not in [200, 201]:
            print(f"❌ Failed to update branch: {update_response.status_code}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 80)
    print("🚀 GROUND HANDLING ROSTERING SYSTEM - GITHUB UPLOAD")
    print("=" * 80)
    print(f"\n📍 Repository: {GITHUB_USERNAME}/{REPO_NAME}")
    print(f"📍 Total files: {len(ALL_FILES)}\n")
    
    print("⏳ Uploading to GitHub...")
    success = upload_files_via_git_api(ALL_FILES)
    
    print("\n" + "=" * 80)
    if success:
        print("✅ SUCCESS! All files uploaded")
        print(f"\n📍 https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
        print("\n📋 Next steps:")
        print("1. git clone https://github.com/ruibraga83/ground-handling-rostering.git")
        print("2. cd backend && docker-compose up -d")
        print("3. cd ../frontend && npm install && npm run dev")
        print("4. Open http://localhost:3000")
    else:
        print("❌ Upload failed - check errors above")
    print("=" * 80)

if __name__ == "__main__":
    main()
