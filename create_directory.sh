#!/bin/bash
# Author : Krishnendu VP
# Purpose: Script to create directories for a Python project
# Usage : ./create_directory.sh
# Tested On : Ubuntu 22.04.1 LTS, GNU bash, version 5.1.16
#

echo "This bash script will create a project directory"
# Get porject name from user input
read -erp "Enter the project name : " project_name
echo "Creating $project_name project directoy structure at ./$project_name"
# Condition to check project creation is successful or not
if mkdir -p "$project_name"/Documentation "$project_name"/Tests "$project_name"/Examples "$project_name"/Source; then
        echo "Successfully created Python project directory structure"
        ls --format=single-column ./"$project_name"
else
        echo "Failed to create directory !!!"
fi


