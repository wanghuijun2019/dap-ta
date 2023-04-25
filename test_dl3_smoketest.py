
import test_dl3
import ParaDef
import TestDef
import TestDef_config

def test_smoke():
    test_dl3.test_inite001(ParaDef.boxIp)

    test_dl3.test_SetAndVerifyPassword()
    test_dl3.test_GetVersions()
    test_dl3.test_setName()
    test_dl3.test_deamon001()
    test_dl3.test_deamon002()
    test_dl3.test_deamon003()
    test_dl3.test_deamon004()
    test_dl3.test_deamon006()
    test_dl3.test_deamon007()
    test_dl3.test_deamon008()
    test_dl3.test_deamon009()
    test_dl3.test_deamon010()
    test_dl3.test_deamon011()
    test_dl3.test_deamon012()
    test_dl3.test_deamon013()
    #  test_dl3.test_Marker001()
    test_dl3.test_deviceInfo001()
    test_dl3.test_deviceInfo002()
    test_dl3.test_deviceInfo003()
    test_dl3.test_deviceInfo005()
    test_dl3.test_GetDeviceUsage()
    test_dl3.test_config_time_001()
    test_dl3.test_file_eso()
    test_dl3.test_config_flowlabels001()
    test_dl3.test_file_can()

    config_test()
    print("run success!")
    return

def config_test():
    token = TestDef.GetToken(ParaDef.deamonIp, ParaDef.uid1, "this is a test!")
    if token == -1:
        assert False, ("test config001 fail, usr1 get token fail")

    retConf = TestDef_config.GetConfig(ParaDef.configIp)

    if retConf == -1 or len(retConf['can']) == 0:
        assert False, ("test config001 fail, get config fail or conf is null")



