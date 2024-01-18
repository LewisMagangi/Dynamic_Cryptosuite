#!/usr/bin/env bash

# Function to update the push script in a directory
update_push_script() {
    local directory="$1"
    local new_push_script="$2"

    # Check if the push script exists in the directory
    if [ -f "$directory/push" ]; then
        # Update the push script
        cp "$new_push_script" "$directory/push"

        # Add and commit the changes
        cd "$directory" || exit
        git add push
        git commit -m "Updating the push script in $directory"
        git push
        cd - || exit
    fi
}

# Main script

# Check if the new push script is provided
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <new_push_script>"
    exit 1
fi

new_push_script="$1"

# Find all directories containing a push script
directories_with_push=($(find . -type f -name "push" -exec dirname {} \; | sort -u))

# Update and push the push script in each directory
for directory in "${directories_with_push[@]}"; do
    update_push_script "$directory" "$new_push_script"
done

echo "Script completed successfully."
