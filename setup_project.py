#!/usr/bin/env python3
"""
Ground Handling Rostering System - Project Setup
Creates all folders and files for the project
"""

import os
import json
from pathlib import Path

def create_file(file_path, content):
    """Create a file with the given content"""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {file_path}")

def setup_project():
    """Create all project folders and files"""
    
    print("=" * 70)
    print("🚀 Ground Handling Rostering System - Project Setup")
    print("=" * 70)
    
    # ============================================================================
    # ROOT FILES
    # ============================================================================
    
    create_file("README.md", """\
# 🚀 Ground Handling Rostering System

A production-ready, multi-tenant SaaS platform for ground handling rostering, task allocation, and staff management across multiple airports.

## Features

- **Multi-Airport Support**: Manage OPO, LIS, FAO, FNC with independent configurations
- **Multi-Tenant Architecture**: Complete data isolation using PostgreSQL Row-Level Security
- **Advanced Task Optimization**: Greedy allocation with Google OR-Tools (maximize utilization or minimize staff)
- **Real-Time Roster Updates**: WebSocket-powered live synchronization
- **Role-Based Access Control**: RBAC per airport/department
- **Comprehensive Exports**: PDF and Excel roster exports
- **Drag-and-Drop Interface**: Manual task allocation with constraint validation

## Tech Stack

- **Frontend**: React 18 + TypeScript + Redux Toolkit + Vite
- **Backend**: Node.js 20 + Express + TypeScript
- **Database**: PostgreSQL 15 with Row-Level Security
- **Cache**: Redis 7
- **Optimization**: Python 3.11 + Google OR-Tools
- **Deployment**: Docker + AWS ECS/Fargate

## Quick Start

### Prerequisites
- Docker Desktop installed
- Node.js 20+ (for frontend development)
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ruibraga83/ground-handling-rostering.git
   cd ground-handling-rostering