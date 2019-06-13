# encoding: utf-8
# module _portaudio
# from C:\Users\N-pod\AppData\Roaming\Python\Python27\site-packages\_portaudio.pyd
# by generator 1.145
# no doc
# no imports

# Variables with simple values

paAbort = 2
paAL = 9
paALSA = 8
paASIO = 3
paBadIODeviceCombination = -9993
paBadStreamPtr = -9988
paBeOS = 10
paBufferTooBig = -9991
paBufferTooSmall = -9990
paCanNotReadFromACallbackStream = -9977
paCanNotReadFromAnOutputOnlyStream = -9975
paCanNotWriteToACallbackStream = -9976
paCanNotWriteToAnInputOnlyStream = -9974
paComplete = 1
paContinue = 0
paCoreAudio = 5
paCustomFormat = 65536
paDeviceUnavailable = -9985
paDirectSound = 1
paFloat32 = 1
paHostApiNotFound = -9979
paIncompatibleHostApiSpecificStreamInfo = -9984
paIncompatibleStreamHostApi = -9973
paInDevelopment = 0
paInputOverflow = 2
paInputOverflowed = -9981
paInputUnderflow = 1
paInsufficientMemory = -9992
paInt16 = 8
paInt24 = 4
paInt32 = 2
paInt8 = 16
paInternalError = -9986
paInvalidChannelCount = -9998
paInvalidDevice = -9996
paInvalidFlag = -9995
paInvalidHostApi = -9978
paInvalidSampleRate = -9997
paJACK = 12
paMME = 2
paNoDevice = -1
paNoError = 0
paNotInitialized = -10000
paNullCallback = -9989
paOSS = 7
paOutputOverflow = 8
paOutputUnderflow = 4
paOutputUnderflowed = -9980
paPrimingOutput = 16
paSampleFormatNotSupported = -9994
paSoundManager = 4
paStreamIsNotStopped = -9982
paStreamIsStopped = -9983
paTimedOut = -9987
paUInt8 = 32
paUnanticipatedHostError = -9999
paWASAPI = 13
paWDMKS = 11

# functions

def abort_stream(*args, **kwargs): # real signature unknown
    """ aborts port audio stream """
    pass

def close(*args, **kwargs): # real signature unknown
    """ close port audio stream """
    pass

def get_default_host_api(*args, **kwargs): # real signature unknown
    """ get default host API index """
    pass

def get_default_input_device(*args, **kwargs): # real signature unknown
    """ get default input device index """
    pass

def get_default_output_device(*args, **kwargs): # real signature unknown
    """ get default output device index """
    pass

def get_device_count(*args, **kwargs): # real signature unknown
    """ get host API count """
    pass

def get_device_info(*args, **kwargs): # real signature unknown
    """ get device information """
    pass

def get_host_api_count(*args, **kwargs): # real signature unknown
    """ get host API count """
    pass

def get_host_api_info(*args, **kwargs): # real signature unknown
    """ get host api information """
    pass

def get_sample_size(*args, **kwargs): # real signature unknown
    """ get sample size of a format in bytes """
    pass

def get_stream_cpu_load(*args, **kwargs): # real signature unknown
    """ returns stream CPU load -- always 0 for blocking mode """
    pass

def get_stream_read_available(*args, **kwargs): # real signature unknown
    """ get buffer available for reading """
    pass

def get_stream_time(*args, **kwargs): # real signature unknown
    """ returns stream time """
    pass

def get_stream_write_available(*args, **kwargs): # real signature unknown
    """ get buffer available for writing """
    pass

def get_version(*args, **kwargs): # real signature unknown
    """ get version """
    pass

def get_version_text(*args, **kwargs): # real signature unknown
    """ get version text """
    pass

def host_api_device_index_to_device_index(*args, **kwargs): # real signature unknown
    """ get default host API index """
    pass

def host_api_type_id_to_host_api_index(*args, **kwargs): # real signature unknown
    """ get default host API index """
    pass

def initialize(*args, **kwargs): # real signature unknown
    """ initialize portaudio """
    pass

def is_format_supported(*args, **kwargs): # real signature unknown
    """ returns whether specified format is supported """
    pass

def is_stream_active(*args, **kwargs): # real signature unknown
    """ returns whether stream is active """
    pass

def is_stream_stopped(*args, **kwargs): # real signature unknown
    """ returns whether stream is stopped """
    pass

def open(*args, **kwargs): # real signature unknown
    """ open port audio stream """
    pass

def read_stream(*args, **kwargs): # real signature unknown
    """ read from stream """
    pass

def start_stream(*args, **kwargs): # real signature unknown
    """ starts port audio stream """
    pass

def stop_stream(*args, **kwargs): # real signature unknown
    """ stops  port audio stream """
    pass

def terminate(*args, **kwargs): # real signature unknown
    """ terminate portaudio """
    pass

def write_stream(*args, **kwargs): # real signature unknown
    """ write to stream """
    pass

# no classes
