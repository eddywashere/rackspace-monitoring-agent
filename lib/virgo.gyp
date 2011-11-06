{
  'targets': [
    {
      'target_name': 'virgolib',
      'type': 'static_library',
      'dependencies': [
        '../deps/http_parser/http_parser.gyp:http_parser',
        '../deps/uv/uv.gyp:uv',
        '../deps/zlib.gyp:zlib',
        '../deps/minizip.gyp:libminizip',
        '../deps/openssl.gyp:openssl',
        '../deps/lua.gyp:lua',
        '../deps/sigar.gyp:sigar',
      ],

      'sources': [
        'virgo_conf.c',
        'virgo_error.c',
        'virgo_init.c',
        'virgo_lua.c',
        'virgo_lua_loader.c',
        'virgo_lua_debugger.c',
        'virgo_portable.c'
        ],
      'include_dirs': [
          '.',
          '../include/private',
          '../include',
        ],
        'direct_dependent_settings': {
          'include_dirs': [
            '../include',
          ],
        },
    }
  ],
}
