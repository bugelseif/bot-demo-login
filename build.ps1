$exclude = @("venv", "bot-demo-login.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-demo-login.zip" -Force