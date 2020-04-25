# mcbackup-azure
Simple Python script that backs up a Minecraft Server to Azure Blob Storage

This script is meant to be used on a server previously set up using the directions from agowa338's [MinecraftSystemdUnit repository](https://github.com/agowa338/MinecraftSystemdUnit).

After doing so, you'll need to append the following line into the minecraft@.service file, after the list of ExecStop commands.

```ExecStop=/bin/bash /opt/minecraft/backup.sh %i```

This causes a backup archive to be sent to Azure's blob storage service every time a minecraft service is stopped using systemd.

Alternatively, the command can also run manually, or via a CRON job.
For instance, to back up a server named "survival" every 4 hours, one would use the following CRON job (as the minecraft user ):

```0 */4 * * * /bin/bash /opt/minecraft/backup.sh survival```
