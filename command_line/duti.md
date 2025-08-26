# Change default application for file types

Install `duti`
```
brew install duti
```

Find the bundle id for the application
```
osascript -e 'id of app "App Name"'

e.g.
osascript -e 'id of app "Preview"'
```

Set Preview as default application for pdf files
```
duti -s com.apple.Preview pdf all
```