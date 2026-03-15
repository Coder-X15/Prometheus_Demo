# GPS Service

A robust GPS tracking service built in Go with Prometheus metrics integration for monitoring.

## Features

- **Location Tracking**: Update and retrieve GPS coordinates for multiple devices
- **Validation**: Validates latitude (-90 to 90) and longitude (-180 to 180) ranges
- **Prometheus Metrics**: Built-in monitoring for:
  - Location update counts per device
  - Active device count
  - Request duration histograms
  - Error tracking and classification
- **Thread-Safe**: Uses RWMutex for concurrent access
- **RESTful API**: Clean HTTP endpoints for location management

## Building

```bash
go build -o gps_service
```

## Running

```bash
./gps_service
```

The service starts on port 8080.

## API Endpoints

### 1. Health Check
```bash
GET /health
```
Returns service health status.

### 2. Update Location
```bash
POST /gps/update
Content-Type: application/json

{
  "id": "device_123",
  "latitude": 40.7128,
  "longitude": -74.0060,
  "accuracy": 5.0,
  "speed": 12.5
}
```
Updates or creates a location for a device.

### 3. Get Location
```bash
# Get all locations
GET /gps/location

# Get specific device location
GET /gps/location?id=device_123
```
Retrieves current location(s).

### 4. Get Statistics
```bash
GET /gps/stats
```
Returns service statistics including active device count.

### 5. Prometheus Metrics
```bash
GET /metrics
```
Exposes Prometheus metrics for monitoring.

## Example Usage

### Update device location
```bash
curl -X POST http://localhost:8080/gps/update \
  -H "Content-Type: application/json" \
  -d '{
    "id": "vehicle_001",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "accuracy": 3.5,
    "speed": 15.2
  }'
```

### Get device location
```bash
curl http://localhost:8080/gps/location?id=vehicle_001
```

### Get all locations
```bash
curl http://localhost:8080/gps/location
```

### View metrics
```bash
curl http://localhost:8080/metrics
```

## Prometheus Metrics

- `gps_location_updates_total` - Counter of location updates per device
- `gps_active_devices` - Gauge of currently tracked devices
- `gps_request_duration_seconds` - Histogram of request latencies
- `gps_errors_total` - Counter of errors by type

## Data Model

```go
type GPSCoordinate struct {
  ID        string    // Device identifier
  Latitude  float64   // -90 to 90
  Longitude float64   // -180 to 180
  Accuracy  float64   // Accuracy in meters
  Timestamp time.Time // When location was recorded
  Speed     float64   // Speed in m/s
}
```

## Dependencies

- `github.com/prometheus/client_golang` - Prometheus metrics client

## Error Handling

The service includes comprehensive error handling for:
- Invalid latitude/longitude values
- Missing device IDs
- Device not found errors
- Invalid request payloads
