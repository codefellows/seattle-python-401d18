# Deployment Check List

## Front End

- Create Next App locally and test it locally
  - Depends on: API
- Deploy Next app
  - Depends on: working locally, GitHub repo in proper shape on main branch (which is default production branch)

## API

- Depends On: DB
- Is it deployed?
- Can you test it? E.g. using ThunderClient
- Are environment vars correct?

## DB

- Depends On: Nothing
- Confirm it's still there at host (e.g. ElephantSQL)
- Needs migration? Migrate as needed
