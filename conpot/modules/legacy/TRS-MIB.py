# PySNMP SMI module. Autogenerated from smidump -f python TRS-MIB
# by libsmi2pysnmp-0.1.1 at Fri Aug 31 13:56:45 2012,
# Python version (2, 6, 6, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

(Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier",
                                                                      "OctetString")
(Bits, Integer32, MibIdentifier, MibScalar, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32",
                                                                                    "MibIdentifier", "MibScalar",
                                                                                    "TimeTicks")

# Objects

internet = MibIdentifier((1, 3, 6, 1))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
thorcom = MibIdentifier((1, 3, 6, 1, 4, 1, 27817))
trs = MibIdentifier((1, 3, 6, 1, 4, 1, 27817, 2))
trsEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 27817, 2, 1))
trsDeliveryTime = MibScalar((1, 3, 6, 1, 4, 1, 27817, 2, 1, 1), Integer32()).setMaxAccess("readonly")

if mibBuilder.loadTexts:
    trsDeliveryTime.setDescription("Average message delivery time in milliseconds.")

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("TRS-MIB", internet=internet, enterprises=enterprises, thorcom=thorcom, trs=trs,
                         trsEntry=trsEntry, trsDeliveryTime=trsDeliveryTime)