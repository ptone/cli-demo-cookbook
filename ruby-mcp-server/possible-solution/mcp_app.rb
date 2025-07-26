require 'sinatra'
require 'socket'
require 'httparty'
require 'json'

class McpApp < Sinatra::Base
  helpers do
    def get_location
      begin
        location_info = HTTParty.get('http://ip-api.com/json').parsed_response
        city = location_info['city']
        country = location_info['country']
        "#{city}, #{country}"
      rescue
        'unknown, unknown'
      end
    end

    def get_uname
      `uname -s`.strip
    end

    def get_hostname
      `hostname -s`.strip
    end

    def get_datetime
      Time.now.iso8601
    end
  end

  # Model Context Protocol Tool: location
  get '/mcp/tools/location' do
    begin
      content_type :json
      { location: get_location }.to_json
    rescue => e
      content_type :json
      status 500
      { error: e.message, backtrace: e.backtrace }.to_json
    end
  end

  # Model Context Protocol Tool: uname
  get '/mcp/tools/uname' do
    begin
      content_type :json
      { uname: get_uname }.to_json
    rescue => e
      content_type :json
      status 500
      { error: e.message, backtrace: e.backtrace }.to_json
    end
  end

  # Model Context Protocol Tool: hostname
  get '/mcp/tools/hostname' do
    begin
      content_type :json
      { hostname: get_hostname }.to_json
    rescue => e
      content_type :json
      status 500
      { error: e.message, backtrace: e.backtrace }.to_json
    end
  end

  # Model Context Protocol Tool: datetime
  get '/mcp/tools/datetime' do
    begin
      content_type :json
      { datetime: get_datetime }.to_json
    rescue => e
      content_type :json
      status 500
      { error: e.message, backtrace: e.backtrace }.to_json
    end
  end

  # Model Context Protocol Tool: error_test
  get '/mcp/tools/error_test' do
    begin
      raise 'This is a permanent error to test error handling.'
    rescue => e
      content_type :json
      status 500
      response = { error: e.message }
      response[:backtrace] = e.backtrace if params['verbose'] == 'true'
      response.to_json
    end
  end

  # Model Context Protocol Tools Listing
  get '/mcp/tools' do
    content_type :json
    {
      tools: [
        {
          name: 'location',
          description: 'Provides the server location (city, country).'
        },
        {
          name: 'uname',
          description: 'Provides the server OS name.'
        },
        {
          name: 'hostname',
          description: 'Provides the server hostname.'
        },
        {
          name: 'datetime',
          description: 'Provides the server datetime.'
        },
        {
          name: 'error_test',
          description: 'Tests the error handling.'
        }
      ]
    }.to_json
  end

  # Sinatra route for the root
  get '/' do
    'Hello from Sinatra!'
  end
end