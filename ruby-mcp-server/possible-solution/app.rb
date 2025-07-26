require 'sinatra'
require 'socket'
require 'json'
require 'httparty'

set :bind, '0.0.0.0'
set :port, 4242

get '/' do
  content_type :json

  # Get location info
  begin
    location_info = HTTParty.get('http://ip-api.com/json').parsed_response
    city = location_info['city']
    country = location_info['country']
    location = "#{city}, #{country}"
  rescue
    location = 'unknown, unknown'
  end

  {
    datetime: Time.now.iso8601,
    hostname: `hostname -s`.strip,
    uname: `uname -s`.strip,
    location: location
  }.to_json
end