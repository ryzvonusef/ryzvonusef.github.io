text

```SQL
ride_id,            STRING
rideable_type,      STRING
started_at,         TIMESTAMP
ended_at,           TIMESTAMP
start_station_name, STRING
end_station_name,   STRING
start_station_id,   INTEGER/STRING (see ** below)
end_station_id,     INTEGER/STRING (see ** below)
start_lat,          FLOAT
start_lng,          FLOAT
end_lat,            FLOAT
end_lng,            FLOAT
member_casual,      STRING
```

```python
def greet(name):
    print(f"Hello, {name}!")
```

```
function test() {
  console.log("notice the blank line before this function?");
}
```

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

```SQL
SELECT *, COUNT(*) 
  FROM t1
 GROUP BY x, y, z, ... -- all attributes of t1

EXCEPT

SELECT *, COUNT(*) 
  FROM t2
 GROUP BY x, y, z, ... -- all attributes of t2
```
