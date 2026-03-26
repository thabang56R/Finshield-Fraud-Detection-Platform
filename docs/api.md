# API

## Endpoints

### GET /
Returns basic service metadata.

### GET /health
Returns health status for the API.

### POST /features/realtime
Generates realtime fraud features from a live transaction payload using historical transaction data.

### POST /rules/evaluate
Evaluates configured fraud rules against the engineered transaction features.

### POST /score/rules
Runs the rule-based fraud scoring engine and returns:
- rule score
- triggered rules
- decision
- top reasons
