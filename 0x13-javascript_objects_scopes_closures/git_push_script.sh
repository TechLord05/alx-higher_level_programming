#!/bin/bash

# Prompt for a commit message
read -p "Enter your commit message: " commit_message

# Add all changes
git add .

# Commit changes with the provided message
git commit -m "$commit_message"

# Push changes to the remote repository
git push
