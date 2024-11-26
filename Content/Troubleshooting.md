# Troubleshooting Guide

## Error 401: Unauthorized
- **Cause**: Invalid or expired authentication token.
- **Solution**: Ensure that the token is valid and has the necessary permissions. Recreate the token if necessary.

## Error 403: Forbidden
- **Cause**: Exceeded API rate limits or access restrictions.
- **Solution**: Check the rate limit using the `GET /rate_limit` endpoint. If rate limits are exceeded, wait until the reset period.

## Rate Limits
- **GitHub Rate Limit**: GitHub imposes a rate limit on the number of requests that can be made within a certain time frame. For authenticated users, the limit is typically higher.
- **Solution**: Monitor the rate limit using the `/rate_limit` endpoint and handle it by waiting for the reset time.
