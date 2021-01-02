$DesktopPath = "$($env:USERPROFILE)\Desktop\faa_eval.lnk"
$FAAPath = Join-Path -Path $(get-location) -ChildPath "\src\main.py"
# Add shortcut to Desktop
$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($DesktopPath)
$Shortcut.TargetPath = $FAAPath
$Shortcut.Save()
$t = Read-Host """faa_eval"" shortcut created on user desktop. Rerun this script if you move the source files. Press ""Enter"" to close this window"