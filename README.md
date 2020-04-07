# Minecraft-UUID-Transfer
Tool for fixing inventories in the transition of a server from online to offline mode.

When transitioning a server to offline mode, the UUIDs of each player will reset, leaving everyone with blank inventories. To solve this, this script will take both the original usercache.json and the new usercache.json and make the conversions accordingly. Backups are made in the ./backups folder.

2 things are required to use this script: all of the old and new UUIDs of each player. For every player you have the new UUID of, remove it from the usercache.json. Rename the usercache.json to a new name (such as usercache-old.json). As players join, their new UUIDs will be in usercache.json. You can now call the python script with the world name, old usercache, and new usercache.

Some notes:

Players must be logged out for the script to work properly. Only the players that have not been copied will be copied, so you don't need to close the server necessarily. You just need to make sure the players who have broken inventories at the moment are logged out. If they remain logged in, there will be undefined behaviours/race conditions with the server that cause the players to lose their inventory. As we are making backups, this isn't an issue, but it means that the player's data must be replaced manually. 
