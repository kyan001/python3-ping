import enum

ICMP_DEFAULT_CODE = 0  # the code for ECHO_REPLY and ECHO_REQUEST


class IcmpType(enum.IntEnum):
    """Enum for Type in ICMP Header."""
    ECHO_REPLY = 0
    ECHO_REPLY_IPV6 = 129
    DESTINATION_UNREACHABLE = 3
    REDIRECT_MESSAGE = 5
    ECHO_REQUEST = 8
    ECHO_REQUEST_IPV6 = 128
    ROUTER_ADVERTISEMENT = 9
    ROUTER_SOLICITATION = 10
    TIME_EXCEEDED = 11
    BAD_IP_HEADER = 12
    TIMESTAMP = 13
    TIMESTAMP_REPLY = 14


class IcmpDestinationUnreachableCode(enum.IntEnum):
    """Enum for Code in ICMP Header when type is DESTINATION_UNREACHABLE (3)"""
    DESTINATION_NETWORK_UNREACHABLE = 0
    DESTINATION_HOST_UNREACHABLE = 1
    DESTINATION_PROTOCOL_UNREACHABLE = 2
    DESTINATION_PORT_UNREACHABLE = 3
    FRAGMENTATION_REQUIRED = 4
    SOURCE_ROUTE_FAILED = 5
    DESTINATION_NETWORK_UNKNOWN = 6
    DESTINATION_HOST_UNKNOWN = 7
    SOURCE_HOST_ISOLATED = 8
    NETWORK_ADMINISTRATIVELY_PROHIBITED = 9
    HOST_ADMINISTRATIVELY_PROHIBITED = 10
    NETWORK_UNREACHABLE_FOR_TOS = 11
    HOST_UNREACHABLE_FOR_TOS = 12
    COMMUNICATION_ADMINISTRATIVELY_PROHIBITED = 13
    HOST_PRECEDENCE_VIOLATION = 14
    PRECEDENCE_CUTOFF_IN_EFFECT = 15


class IcmpTimeExceededCode(enum.IntEnum):
    """Enum for Code in ICMP Header when type is TIME_EXCEEDED (11)"""
    TTL_EXPIRED = 0
    FRAGMENT_REASSEMBLY_TIME_EXCEEDED = 1
