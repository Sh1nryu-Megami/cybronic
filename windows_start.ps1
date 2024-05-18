if ($args.count -lt 1) {
  & docker-compose.exe up
} else {
  Set-Location .\math_module
  $view = & python config_getter.py -v | Out-String
  $view = $view.Substring(0, $view.Length - 2)
  $layout = & python config_getter.py -l | Out-String
  $layout = $layout.Substring(0, $layout.Length - 2)
  $ip = & python config_getter.py -h | Out-String
  $ip = $ip.Substring(0, $ip.Length - 2)
  
  Copy-Item -Force -Path $layout -Destination .\data\layout.json
  Write-Output "Layout Copied into math_module\data"
  Copy-Item -Force -Path $layout -Destination ..\backend\data\layout.json
  Copy-Item -Force -Path $view -Destination ..\backend\data\view.svg
  Write-Output "View and Layout copied to backend\data"
  
  Set-Location ..\front\map
  & python .\setup.py --ip $ip
  & npm install
  & npm run build
  
  New-Item -Force -ItemType Directory -Path ..\..\backend\data\dist\
  Copy-Item -Force -Path .\dist\* -Destination ..\..\backend\data\dist
  
  New-Item -Force -ItemType Directory -Path ..\..\backend\data\dist\assets\
  Copy-Item -Force -Path .\dist\assets\* -Destination ..\..\backend\data\dist\assets\
  
  Write-Output "All compiled frontend files moved to backend\data\"
  
  Set-Location ..\..\backend\
  
  Write-Output "All composer modules installed"
  
  Set-Location ..

  & docker-compose.exe build
  & docker-compose.exe up 
}
