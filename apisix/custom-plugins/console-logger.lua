-- custom_plugin/request_logger.lua

local core = require("apisix.core")

local plugin_name = "request-logger"

local _M = {
    version = 0.1,
    priority = 10,  -- Plugin execution priority
    name = plugin_name,
}

function _M.check_schema(conf)
    -- Add schema validation if needed
    return true
end

function _M.access(conf, ctx)
    -- Log the incoming request details
    core.log.info("Request received: ", core.request.get_host(ctx), core.request.get_uri(ctx))
end

return _M
