-- lua/custom/add-header.lua

local plugin_name = "add-header"

local schema = {
    type = "object",
    properties = {
        header_name = { type = "string" },
        header_value = { type = "string" }
    },
    required = { "header_name", "header_value" },
}

local _M = {
    version = 0.1,
    priority = 10,  -- set higher priority if needed
    name = plugin_name,
    schema = schema,
}

function _M.check_schema(conf)
    return core.schema.check(schema, conf)
end

function _M.header_filter(conf, ctx)
    -- Add the custom header
    ngx.header[conf.header_name] = conf.header_value
end

return _M
