one_valid_endpoint = [
    {
        "addr": "1.1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    }
]

one_invalid_endpoint = [
    {
        "addr": "191.111.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    }
]

three_valid_endpoints = [
    {
        "addr": "1.1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "Google DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "Google DNS",
        "ignore": False
    }
]

two_valid_one_invalid_endpoints = [
    {
        "addr": "1.1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "Google DNS",
        "ignore": False
    },
    {
        "addr": "191.111.1.1",
        "description": "Google DNS",
        "ignore": False
    }
]

two_valid_ignored = [
    {
        "addr": "1.1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "Google DNS",
        "ignore": True
    }
]

twelve_valid_endpoints = [
    {
        "addr": "1.1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "Google DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "Google DNS",
        "ignore": False
    },
    {
        "addr": "1.1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "Google DNS",
        "ignore": False
    },
    {
        "addr": "1.1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "Google DNS",
        "ignore": False
    },
    {
        "addr": "1.1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "Google DNS",
        "ignore": False
    },
    {
        "addr": "1.1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "11th DNS",
        "ignore": False
    },
    {
        "addr": "8.8.8.8",
        "description": "12th DNS",
        "ignore": False
    }
]

invalid_ip = [
    {
        "addr": "1.1.1",
        "description": "Cloudflare DNS",
        "ignore": False
    }
]

invalid_data_type = [
    {
        "addr": "test",
        "description": "",
        "ignore": "test"
    }
]
