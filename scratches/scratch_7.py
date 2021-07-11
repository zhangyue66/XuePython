'''
TrafficSimulatorLib.py -  This module contains all superscript landslide
config  methods
'''

import traceback
import re
import json
import RobotLogger
from UtilitiesLib import UtilitiesLib


class TrafficSimulatorLib:
    """
    ##########################################################################
        Title          : TrafficSimulatorLib
        Description    : This class contains all superscript landslide
                         config methods
        Author(s)      : PhanisreeY(py1780), Paulo Nicholas A(pa685w)
        Date           : 09/17/2018
        python_version : 3.5.2
    ##########################################################################
    """

    def __init__(self):
        pass

    def config_dra_node(self, conf_obj, input_dict, landslide_object, node_index, tc_script_json,
                        phy_eth_names_list):
        """
        ######################################################################
            Title          : config_dra_node()
            Description    : Configure DRA Node parameters for Landslide configuration.
            Parameters     : conf_obj - Json object is obtained from any of the
                                    "framing" methods in LandslideRest Class
                                    or Basic json structure of the landslide parameters
                                    Ex - {'tsGroups':
                                    [{'testCases': [{'type': '', 'name': '','parameters': {}}
                             input_dict - Landslide object
                             landslide_object - landslide_object
                             node_index - Index of the test case where to add the sgw control addr
                             tc_script_json - Json output of the landslide script.
                             phy_eth_names_list - Physical Ethernet names with seperated by space
                                    Ex: ["eth1", "eth2", "eth3"]
            Return Value   : True - if test session configured successfully
                             False - if test session configured failed or
                             Exception while configuring test session
            Version  Author                 Date        Remarks
            0.1     Debasish Nayak(dn8492) 10/08/2018  Initial Draft
        ######################################################################
        """
        return_flag = "True"
        reserve_ports = 0
        mog_dict = {"Gen2ClnNodeHost": input_dict['mogDetails']['mogOriginHost'],
                    "Gen2ClnNodeRealm": input_dict['mogDetails']['mogOriginRealm'],
                    "PCRFClnCcMsisdn": input_dict['ue1Details']['msisdn1'],
                    "PCRFClnCcImsi": input_dict['ue1Details']['imsi1'],
                    "SutHost1": "*.realm",
                    "SutRealm1": input_dict['mogDetails']['mogPASRealm'],
                    "SutPort1": input_dict['mogDetails']['mogPASPort']}
        mog_config = landslide_object.frame_landslide_parameters(
            conf_obj, mog_dict, "", "Dra Nodal", node_index['dra_index'])
        if mog_config['Status'] is True:
            conf_obj = mog_config['conf_obj']
            RobotLogger.log_logger.info("Config mog parameters: %s" % (conf_obj))
        else:
            return {'Status': False,
                    'Error': "Unable to configure mog parameters for the landslide test script"}
        # Frame node parameters for Gen2ClnNodeAddr
        mog_node_config = landslide_object.frame_node_parameters(conf_obj, 'Gen2ClnNodeAddr',
                                                                 input_dict['mogDetails'][
                                                                     'mogIp'],
                                                                 input_dict['mogDetails'][
                                                                     'mogGwIp'],
                                                                 1,
                                                                 input_dict['mogDetails'][
                                                                     'mogPort'],
                                                                 1500, '',
                                                                 input_dict['chassisDetails'][
                                                                     'mogVlan'],
                                                                 node_index['dra_index'])
        reserve_ports = reserve_ports + 1
        # mog_port = input_dict['mogDetails']['mogPort'].replace("v6", "")
        phy_eth_names_list.append(input_dict['mogDetails']['mogPort'].replace("v6", ""))
        if mog_node_config['Status'] is True:
            conf_obj = mog_node_config['conf_obj']
            RobotLogger.log_logger.info("Configure Gen2ClnNode node parameters: %s" % (conf_obj))
        else:
            return {'Status': False,
                    'Error': "Unable to configure Gen2ClnNode node parameters for the landslide test script"}
        # Frame and modify avp parameters
        if ("QPP_DATA_IR9" in input_dict['scenario']) or ("DATA_IR92" in input_dict['scenario']):
            avp_dict = {"apn1": input_dict['apn1Details']['apn1Name'],
                        "apn2": input_dict['apn2Details']['apn2Name']}
        else:
            avp_dict = {"apn1": input_dict['apn1Details']['apn1Name']}
        mog_avp_config = landslide_object.frame_avp_parameters(conf_obj, avp_dict, "Gen2ProfileAvp",
                                                               node_index['dra_index'],
                                                               tc_script_json)
        if mog_avp_config['Status'] is True:
            conf_obj = mog_avp_config['conf_obj']
            RobotLogger.log_logger.info("Mog AVP Parameters framed successfully")
        else:
            return {'Status': False,
                    'Error': "Unable to modify and configure avp parameters for the landslide test script"}
        # Framing DRA sut details for Landslide Test Session
        dra_sut_ip = input_dict['mogDetails']['mogPASIP']
        dra_sut_ip = dra_sut_ip.replace(".", "_")

        dra_sut = landslide_object.add_sut(input_dict['mogDetails']['mogPASIP'],
                                           input_dict['mogDetails']['mogPASIP'],
                                           dra_sut_ip)
        if dra_sut['Status'] is True:
            # conf_obj = sgw_sut_param['conf_obj']
            RobotLogger.log_logger.info("Created DRA SUT Object: %s" % (conf_obj))
        else:
            return {'Status': False,
                    'Error': "Unable to Create DRA sut parameters for the landslide test script"}

        dra_sut_param = landslide_object.frame_sut_parameters(conf_obj, "SutPrimary1", dra_sut_ip,
                                                              node_index['dra_index'])
        if dra_sut_param['Status'] is True:
            conf_obj = dra_sut_param['conf_obj']
            RobotLogger.log_logger.info("DRA SUT Object: %s" % (conf_obj))
        else:
            return {'Status': False,
                    'Error': "Unable to configure mog DRA sut parameters for the landslide test script"}
        if return_flag == "True":
            return {'Status': True, 'conf_obj': conf_obj, 'phy_eth_names_list': phy_eth_names_list}

    def config_ims_node(self, conf_obj, input_dict, landslide_object, node_index,
                        tc_script_json, phy_eth_names_list):
        """
        ######################################################################
            Title          : config_ims_node()
            Description    : Configure IMS Node parameters for Landslide configuration.
            Parameters     : conf_obj - Json object is obtained from any of the
                                    "framing" methods in LandslideRest Class
                                    or Basic json structure of the landslide parameters
                                    Ex - {'tsGroups':
                                    [{'testCases': [{'type': '', 'name': '','parameters': {}}
                             input_dict - Landslide object
                             landslide_object - landslide_object
                             node_index - Index of the test case where to add the sgw control addr
                             tc_script_json - Json output of the landslide script.
                             phy_eth_names_list - Physical Ethernet names with seperated by space
                                    Ex: ["eth1", "eth2", "eth3"]
            Return Value   : True - if test session configured successfully
                             False - if test session configured failed or
                             Exception while configuring test session
            Version  Author                 Date        Remarks
            0.1     Debasish Nayak(dn8492) 10/08/2018  Initial Draft
        ######################################################################
        """
        return_flag = "True"
        tc_name = ""
        tc_type = ""
        # dmz_port = ""
        # rx_port = ""
        reserve_ports = 0
        ims_param_dict = {'TxClnSutPrimaryHost': '*.' + input_dict['diameterDetails'][
            'destinationRealm'],
                          'TxClnSutPrimaryRealm': input_dict['diameterDetails']['destinationRealm'],
                          'TxClnSutPort': input_dict['diameterDetails']['destinationHost'],
                          'TxClnOriginHost': input_dict['RxDetails']['originHost'],
                          'TxClnOriginRealm': input_dict['RxDetails']['originRealm'],
                          'SipSubscriberUriScheme': '0', 'SipEndpointUriScheme': '1',
                          'CommandMode': 'Off',
                          'ImsMode': 'Endpoint', 'ImsApn': input_dict['apn2Details']['apn2Name'],
                          'ImsInterface': 'Gm', 'RxEn': 'true', 'SipRegExpires': '600000',
                          'NumUes': input_dict['ue1Details']['ueCount'],
                          'SipSubscribersPerUe': input_dict['ue1Details']['ueCount'],
                          'PCRFClnCcMsisdnEn': 'true',
                          'PCRFClnCcMsisdn': input_dict['ue1Details']['msisdn1'],
                          'ImsNodeStartingRtpAudioPort': 6000,
                          'ImsNodeStartingRtpVideoPort': 7000, 'ImsNodeStartingMsrpPort': 2855,
                          'ImsNodeStartingRttPort': 8000, 'ImsNodeCallStart': '1',
                          'SipTransport': 'UDP',
                          'SipMaxMsgBufferSize': '2048', 'TxClnConfigMcdEn': 'true'}

        if (("WO_NETLOC" in input_dict['scenario']) or ("REGISTRATION " in input_dict['scenario'])):
            ims_param_dict['ImsNodeNetLocEn'] = "false"
        else:
            ims_param_dict['ImsNodeNetLocEn'] = "true"
        if (("IR9" in input_dict['scenario']) or ("REGISTRATION" in input_dict['scenario'])):
            temp_dict = {'TxClnCodecEn_0': 'true', 'TxClnNumCodecs_0': '2',
                         'TxClnAFAppIdent_0': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                         'TxClnMaxReqUL_0': '38000',
                         'TxClnMaxReqDL_0': '38000', 'TxClnRRBandwidth_0': '1425',
                         'TxClnRSBandwidth_0': '475',
                         'TxClnFlowStatus_0': '2', 'RtpTrafficEn': 'true',
                         'RtpDmf1Type': 'Audio',
                         'RtpTrafficStartDelay': '1000'}
            ims_param_dict = {**ims_param_dict, **temp_dict}
            del temp_dict
            if "MT_Early_Media" in input_dict['scenario']:
                temp_dict = {'ImsNodeCallPending': '1000',
                             'ImsNodeCallLength': 'simulator/audioDuration'}
                ims_param_dict = {**ims_param_dict, **temp_dict}
                del temp_dict
            if "REGISTRATION" in input_dict['scenario']:
                dial_plan_usr = "#(" + input_dict["dialPlanUser"] + ")"
                temp_dict = {'ImsSrvProfilePublicUserName': dial_plan_usr,
                             'ImsSrvProfilePrivateUserName': dial_plan_usr}
                ims_param_dict = {**ims_param_dict, **temp_dict}
                del temp_dict
            if "IR94" in input_dict['scenario']:
                temp_dict = {'RtpDmf2Type': 'Video', 'TxClnCodecEn_1': 'true',
                             'TxClnNumCodecs_1': '2',
                             'TxClnAFAppIdent_1': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                             'TxClnMaxReqUL_1': '38000',
                             'TxClnMaxReqDL_1': '38000', 'TxClnRRBandwidth_1': '1425',
                             'TxClnRSBandwidth_1': '475',
                             'TxClnFlowStatus_1': '2', 'SipRegEn': 'true',
                             'ImsNodeFunctionalityPattern': '3'}
                ims_param_dict = {**ims_param_dict, **temp_dict}
                del temp_dict
                if "downgrade" in input_dict['scenario']:
                    temp_dict = {'UeVideoDelay': '0', 'UeReleaseMode': 'VideoFirst',
                                 'UeVideoDuration': 'simulator/videoTimer'}
                    ims_param_dict = {**ims_param_dict, **temp_dict}
                    del temp_dict
            if "EMERGENCY" in input_dict['scenario']:
                ims_param_dict['EmergencyEn'] = True
            if "IPME" in input_dict['scenario']:
                temp_dict = {'TxClnAFAppIdent_2': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                             'TxClnMaxReqUL_2': '1024000',
                             'TxClnMaxReqDL_2': '1024000',
                             'TxClnFlowStatus_2': '2', 'MsrpSendMessagesEn': 'true',
                             'MsrpStartDelay': '1000', 'MsrpInterval': '1000', 'MsrpEn': 'true',
                             'TxClnMaxReqUL_3': '330', 'TxClnMaxReqDL_3': '330'}
                ims_param_dict = {**ims_param_dict, **temp_dict}
                del temp_dict
            if "RTT" in input_dict['scenario']:
                temp_dict = {'RtpDmf2Type': 'RTT', 'TxClnCodecEn_3': 'true',
                             'TxClnNumCodecs_3': '2',
                             'TxClnAFAppIdent_3': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                             'TxClnMaxReqUL_3': '38000',
                             'TxClnMaxReqDL_3': '38000',
                             'TxClnRRBandwidth_3': '1425', 'TxClnRSBandwidth_3': '475',
                             'TxClnFlowStatus_3': '2', 'SipRegEn': 'true'}
                ims_param_dict = {**ims_param_dict, **temp_dict}
                del temp_dict

        elif "IPME" in input_dict['scenario']:
            temp_dict = {'TxClnAFAppIdent_2': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                         'TxClnMaxReqUL_2': '1024000',
                         'TxClnMaxReqDL_2': '1024000', 'TxClnFlowStatus_2': '2',
                         'MsrpSendMessagesEn': 'true',
                         'MsrpStartDelay': '1000', 'MsrpInterval': '1000',
                         'SipRegEn': 'true', 'MsrpEn': 'true',
                         'ImsNodeFunctionalityPattern': '3'}
            ims_param_dict = {**ims_param_dict, **temp_dict}
            del temp_dict

        # Configure the ims node landslide parameters

        ls_param = landslide_object.frame_landslide_parameters(conf_obj, ims_param_dict,
                                                               tc_name, tc_type,
                                                               node_index['ims_index'])
        if ls_param['Status'] is True:
            conf_obj = ls_param['conf_obj']
            RobotLogger.log_logger.info("Config ims_node parameters: %s" % (conf_obj))
        else:
            RobotLogger.log_logger.info(
                "Unable to configure ims node parameters: %s" % ims_param_dict)
            return {'Status': False,
                    'Error': "Unable to configure af parameters for the landslide test script"}

        # Framing TxClnSutPrimarySrv sut details for Landslide Test Session

        diameter_ip = input_dict["diameterDetails"]["diameterIp"]
        diameter_ip = diameter_ip.replace(":", "_")
        ims_sut = landslide_object.add_sut(input_dict["diameterDetails"]["diameterIp"],
                                           input_dict["diameterDetails"]["diameterIp"], diameter_ip)
        if ims_sut['Status'] is True:
            # conf_obj = sgw_sut_param['conf_obj']
            RobotLogger.log_logger.info("Created IMS SUT Object: %s" % (conf_obj))
        else:
            return {'Status': False,
                    'Error': "Unable to Create IMS sut parameters for the landslide test script"}

        ims_sut_param = landslide_object.frame_sut_parameters(conf_obj, "TxClnSutPrimarySrv",
                                                              diameter_ip,
                                                              node_index['ims_index'])
        if ims_sut_param['Status'] is True:
            conf_obj = ims_sut_param['conf_obj']
            RobotLogger.log_logger.info("Config volte sut parameters details: %s" % (conf_obj))
        else:
            return {'Status': False,
                    'Error': "Unable to configure volte sut parameters for the landslide test script"}

        # Frame and modify avp parameters

        if re.search("SOS", input_dict['apn1Details']['apn1Name'], re.IGNORECASE):
            avp_dict = {"Service-URN": input_dict['serviceURN']}
            sos_avp_config = landslide_object.frame_avp_parameters(conf_obj, avp_dict, "TxClnVsa",
                                                                   node_index['ims_index'],
                                                                   tc_script_json)
            if sos_avp_config['Status'] is True:
                conf_obj = sos_avp_config['conf_obj']
                RobotLogger.log_logger.info("sos Parameters framed successfully")
            else:
                return {'Status': False,
                        'Error': "Unable to modify and configure sos parameters for sos apn in the landslide test script"}

        # Frame node parameters

        sip_outbound_port = input_dict['sipDetails']['sipPort'].replace("v6", "")
        # dmz_port = sip_outbound_port
        af_outbound_port = input_dict['RxDetails']['RxPort'].replace("v6", "")
        # rx_port = AfOutboundPort
        sip_node_param = landslide_object.frame_node_parameters(conf_obj, "SipPCSCFAddr",
                                                                input_dict['sipDetails']['sipIp'],
                                                                input_dict['sipDetails']
                                                                ['sipGwIp'], 1,
                                                                input_dict['sipDetails']
                                                                ['sipPort'], 1500,
                                                                sip_outbound_port,
                                                                input_dict['chassisDetails']
                                                                ['giVlan'],
                                                                node_index['ims_index'])
        reserve_ports = reserve_ports + 1
        phy_eth_names_list.append(input_dict['sipDetails']['sipPort'].replace("v6", ""))
        if sip_node_param['Status'] is True:
            conf_obj = sip_node_param['conf_obj']
            RobotLogger.log_logger.info("sip node parameters framed successfully: %s" % (conf_obj))
        else:
            return {'Status': False,
                    'Error': "Unable to configure sip node parameters for the landslide test script"}
        if "QPP_IMS" in input_dict['scenario']:
            # rx_port=sipOutboundPort
            af_node_param = landslide_object.frame_node_parameters(conf_obj, "AfNodeIpAddr",
                                                                   input_dict['RxDetails']['RxIp'],
                                                                   input_dict['RxDetails']['RxGwIp']
                                                                   , 1,
                                                                   input_dict['RxDetails']['RxPort']
                                                                   , 1500,
                                                                   sip_outbound_port,
                                                                   input_dict['chassisDetails']
                                                                   ['giVlanSupportZone'],
                                                                   node_index['ims_index'])
            reserve_ports = reserve_ports + 1
            phy_eth_names_list.append(input_dict['RxDetails']['RxPort'].replace("v6", ""))
            if af_node_param['Status'] is True:
                conf_obj = af_node_param['conf_obj']
                RobotLogger.log_logger.info("Ims Parameters framed successfully")
            else:
                return {'Status': False,
                        'Error': "Unable to configure af node parameters for the landslide test script"}
        else:
            af_outbound_port = input_dict['RxDetails']['RxPort'].replace("v6", "")
            # rx_port=AfOutboundPort
            af_node_param = landslide_object.frame_node_parameters(conf_obj, "AfNodeIpAddr",
                                                                   input_dict['RxDetails']['RxIp'],
                                                                   input_dict['RxDetails']
                                                                   ['RxGwIp'], 1,
                                                                   input_dict['RxDetails']
                                                                   ['RxPort'], 1500,
                                                                   af_outbound_port,
                                                                   input_dict['chassisDetails']
                                                                   ['giVlanSupportZone'],
                                                                   node_index['ims_index'])
            reserve_ports = reserve_ports + 1
            phy_eth_names_list.append(input_dict['RxDetails']['RxPort'].replace("v6", ""))
            if af_node_param['Status'] is True:
                conf_obj = af_node_param['conf_obj']
                RobotLogger.log_logger.info("Ims Parameters framed successfully")
            else:
                return {'Status': False,
                        'Error': "Unable to configure af node parameters for the landslide test script"}

        if return_flag == "True":
            return {'Status': True, 'conf_obj': conf_obj, 'phy_eth_names_list': phy_eth_names_list}

    def calculate_max_bit_rate(self, max_bit_rate):
        """
            ######################################################################
                Title          : calculate_max_bit_rate()
                Description    : calculate max_bit_rate for Landslide 3GGN configuration.
                Parameters     : max_bit_rate - For Uplink max bit rate or downlink max bit rate
                Return Value   : Uplink/downlink bit rate
                                 False - if test session configured failed or
                                 Exception while configuring test session
                Version  Author                 Date        Remarks
                0.1     Phanisree Y(py1780)   10/15/2018  Initial Draft
            ######################################################################
            """
        max_bit_rate = int(max_bit_rate)
        if max_bit_rate == 0:
            return 255
        elif 1 >= max_bit_rate <= 63:
            return max_bit_rate
        elif 64 >= max_bit_rate <= 568:
            temp = (((max_bit_rate - 64) / 8) + 64)
            return temp
        elif 576 >= max_bit_rate <= 8640:
            temp = (((max_bit_rate - 576) / 64) + 128)
            return temp
        elif 8700 >= max_bit_rate <= 15999:
            temp = ((max_bit_rate - 8600) / 100)
            return temp
        elif 16000 >= max_bit_rate <= 127999:
            temp = (((max_bit_rate - 16000) / 1000) + 74)
            return temp
        elif 128000 >= max_bit_rate <= 256000:
            temp = (((max_bit_rate - 128000) / 2000) + 186)
            return temp
        else:
            return False

    def configure_dmz_ip(self, input_dict, landslide_object, node_index, conf_obj, home_addr_type):
        """
           ######################################################################
               Title          : configure_dmz_ip()
               Description    : This method is used to configure nodes NetworkHostAddrLocal,
                                Ipv4NetworkHostAddrLocal, Ipv6NetworkHostAddrLocal.
               Parameters     : input_dict - Landslide input parameters dictionary
                              : landslide_object - Object to invoke the method frame_node_parameters
                                from the landslide rest class
                              : node_index - gn or gi index
                              : conf_obj - Json rest object
               Return Value   : True - if test session dmz configured successfully
                                False - if test session dmz configuration failed or
                                Exception while configuring test session
               Version  Author                 Date        Remarks
               0.1     Phanisree Y(py1780)   10/17/2018    NIMB-6441 Initial Draft
           ######################################################################
           """
        if home_addr_type == "3":
            enable_node = 1
            node_name = "Ipv4NetworkHostAddrLocal"
        else:
            enable_node = 0
            node_name = "NetworkHostAddrLocal"
        dmz_v4_node_param = landslide_object.frame_node_parameters(
            conf_obj, node_name,
            input_dict['dmz1Details']['dmz1Ip'],
            input_dict['dmz1Details']['dmz1GwIp'], "1",
            input_dict['dmz1Details']['dmz1PhyName'], 1500,
            "", input_dict['chassisDetails']['giVlan'],
            node_index, enable_node)
        if dmz_v4_node_param['Status'] is True:
            conf_obj = dmz_v4_node_param['conf_obj']
        else:
            return {'Status': 'False', 'Error': "DMZv4 frame_node_parameters failed"}
        if home_addr_type == "3":
            dmz_v6_node_param = landslide_object.frame_node_parameters(
                conf_obj, "Ipv6NetworkHostAddrLocal",
                input_dict['dmz1Details']['dmz1Ipv6'],
                input_dict['dmz1Details']['dmz1GwIpv6'], "1",
                input_dict['dmz1Details']['dmz1PhyNamev6'], 1500,
                "", input_dict['chassisDetails']['giVlan'],
                node_index, enable_node)
            if dmz_v6_node_param['Status'] is True:
                conf_obj = dmz_v6_node_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "DMZv6 frame_node_parameters failed"}
        return {'Status': True, 'conf_obj': conf_obj}

    def configure_traffic(self, conf_obj, library_id, gn_param_dict, input_dict,
                          landslide_object, node_index,
                          traffic_list, phy_eth_names_list, home_addr_type, network_host):
        """
            ######################################################################
                Title          : configure_traffic()
                Description    : Configure the trafficTypes, DMZ IPs for landslide traffic
                                 configuration.
                Parameters     : conf_obj - Json object is obtained from any of the
                                    "framing" methods in LandslideRest Class
                                    or Basic json structure of the landslide parameters
                                    Ex -
                            {'tsGroups': [{'testCases': [{'type': '', 'name': '','parameters': {}}
                             input_dict - Landslide object
                             landslide_object - landslide_object
                             node_index - Index of the test case where to add the sgw control addr
                             home_addr_type - PDN Type.
                             gn_param_dict - gn_param_dict for gn config.
                             traffic_list - Traffic List Details (HTTP, FTP, DNS)
                             phy_eth_names_list - Physical Ethernet names with seperated by space
                                    Ex: ["eth1", "eth2", "eth3"]
            Return Value   : True - if test session configured successfully
                             False - if test session configured failed or
                             Exception while configuring test session
            Version  Author                  Date        Remarks
            0.1     Debasish Nayak(dn8492)   10/17/2018  Initial Draft
            0.2     Phanisree Y(py1780)      10/18/2018  [NIMB-6441]Enhanced the method to support
                                                         HTTP Addressable trafffic ipv4v6.
            0.3     Paulo Nicholas A(pa685w) 10/25/2018  [NIMB-6417]Enhanced to support Enterprise
                                                        Service
            0.4     Phanisree Y(py1780)    10/26/2018  [NIMB-6449]Enhance the procedure to invoke
                                                       configure_dmz_ip if the networkHost is local
            0.5     Aman                   11/14/2018   [NIMB-6705] UDP Traffic Gi Traffic added
            0.6     Aman                   12/10/2018    [NIMB-6851] Added TCP support
             ######################################################################
            """
        # dmzOutboundPort = ""
        reserve_ports = 0
        tc_name = ""
        tc_type = ""
        traffic_mtu = 1400
        if network_host == "Local":
            dmz_node_param = self.configure_dmz_ip(
                input_dict, landslide_object, node_index['gn_index'], conf_obj, home_addr_type)
            reserve_ports = reserve_ports + 1
            phy_eth_names_list.append(input_dict['dmz1Details']['dmz1PhyName'].replace("v6", ""))
            if dmz_node_param['Status'] is True:
                conf_obj = dmz_node_param['conf_obj']
                RobotLogger.log_logger.info("dmz_node_param details: %s" % dmz_node_param['conf_obj'])
            else:
                RobotLogger.log_logger.debug("Unable to Frame DMZ Parameters")
                return {'Status': False,
                        'Error': "Unable to configure dmz node parameters for the landslide test script"}
            # Traffic Type Configuration
            for traffic in traffic_list:
                ls_param = landslide_object.frame_dmf_parameters(conf_obj, traffic, library_id,
                                                                 traffic_list,
                                                                 [input_dict['dmz1Details'][
                                                                      'dmz1Ip']],
                                                                 node_index['gn_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
                RobotLogger.log_logger.info("dmf_node_param details: %s" % (ls_param))
            else:
                RobotLogger.log_logger.debug("Unable to Frame DMF Parameters")
                return {'Status': 'False',
                        'Error': "Unable to configure DMF node parameters for the landslide test script"}

        else:

            # Configure Traffic on Gn - SGW Nodal/PGW Nodal
            gn_param_dict['network_host'] = "Remote"

            remote_network_host_addr = []
            traffic_list_upper = [element.upper() for element in traffic_list]
            if any("HTTP_PORT" in item for item in traffic_list_upper):
                remote_network_host_addr.append(input_dict['dmz1Details']['dmz1Ip'])
                RobotLogger.log_logger.info("remote_network_host_addr List: %s" % (remote_network_host_addr))
            elif any("FTP" in item for item in traffic_list_upper):
                remote_network_host_addr.append(input_dict['dmz1Details']['dmz1Ip'])
            elif any("UDP" in item for item in traffic_list_upper):
                remote_network_host_addr.append(input_dict['dmz1Details']['dmz1Ip'])
            elif any("TCP" in item for item in traffic_list_upper):
                remote_network_host_addr.append(input_dict['dmz1Details']['dmz1Ip'])
            if any("FTP_A" in item for item in traffic_list_upper):
                if int(home_addr_type) == 2:
                    ftp_index = traffic_list.index('FTP_Active')
                    traffic_list[ftp_index] = 'FTP_Active_IPv6'
            if any("HTTP_ADDRESSABLE" in item for item in traffic_list_upper):
                if int(home_addr_type) == 1:
                    remote_network_host_addr.append(input_dict['trafficTypeIpList'][
                                                        'httpAddressableIPv4'])
                    RobotLogger.log_logger.info(
                        "HTTP_ADDRESSABLE_IP: %s" % (input_dict['trafficTypeIpList'][
                            'httpAddressableIPv4']))
                elif int(home_addr_type) == 2:
                    remote_network_host_addr.append(input_dict['trafficTypeIpList'][
                                                        'httpAddressableIPv6'])
                elif int(home_addr_type) == 3:
                    remote_network_host_addr.append(input_dict['trafficTypeIpList'][
                                                        'httpAddressableIPv4'])
                    remote_network_host_addr.append(input_dict['trafficTypeIpList'][
                                                        'httpAddressableIPv6'])
                    addr_index = traffic_list.index('HTTP_Addressable')
                    traffic_list.insert(addr_index + 1, 'HTTP_Addressable_IPv6')
            if any("DNS" in item for item in traffic_list_upper):
                remote_network_host_addr.append(input_dict['trafficTypeIpList']['dnsIp'])
            if any("DNS_RECURSIVE" in item for item in traffic_list_upper):
                # remote_network_host_addr.append(input_dict['trafficTypeIpList']['dnsIp'])
                # Create TDF (.csv) file in log path
                tdf_file_name = "dns_traffic.csv"
                data_header = "DNS Server IP, DNS Dest"
                server_ip = input_dict['trafficTypeIpList']['dnsIp']
                dns_dest = input_dict['trafficTypeIpList']['dnsIp']
                data = data_header + "\n" + server_ip + "," + dns_dest
                file_name = input_dict['logsPath'] + "/" + tdf_file_name
                RobotLogger.log_logger.debug("TDF File Name:%s" % (file_name))
                RobotLogger.log_logger.debug("TDF File Data:%s" % (data))
                try:
                    file_handle = open(file_name, "w+")
                    file_handle.write(data)
                    file_handle.close()
                except IOError:
                    RobotLogger.log_logger.debug("IOError occurred while creating tdf file.")
                except Exception as error:
                    print('Error: TDF File: File does not exists: {}'.format(error))
                # Add tdf file
                add_tdf = landslide_object.add_tdf(library_id, input_dict['logsPath'],
                                                   tdf_file_name)

                if add_tdf['Status'] is True:
                    # conf_obj = add_tdf['conf_obj']
                    RobotLogger.log_logger.info("add_tdf file Details: %s" % add_tdf)
                else:
                    RobotLogger.log_logger.debug("Unable to add_tdf files Parameters")
                    return {'Status': False,
                            'Error': "Unable to add_tdf files parameters for the landslide test script"}
            if any("UDP_TDF" in item for item in traffic_list_upper):
                tdf_file_name = "udp.csv"
                dataHeader = "Response Size, IP Segment Size"
                payloadSize = input_dict['trafficDetails']['payloadSize']
                segmentSize = input_dict['trafficDetails']['ueMaxIpSegmentSize']
                # payloadSize = 512
                data = dataHeader + "\n" + str(payloadSize) + "," + str(segmentSize)
                fileName = input_dict['logsPath'] + "/" + tdf_file_name
                RobotLogger.log_logger.debug("TDF File Name:%s" % (fileName))
                RobotLogger.log_logger.debug("TDF File Data:%s" % (data))
                try:
                    fh = open(fileName, "w+")
                    fh.write(data)
                    fh.close()
                except IOError:
                    RobotLogger.log_logger.debug("IOError occurred while creating tdf file.")
                except Exception as error:
                    print('Error: TDF File: File does not exists: {}'.format(error))
                # Add tdf file
                add_TDF = landslide_object.add_tdf(library_id, input_dict['logsPath'], tdf_file_name)

                if (add_TDF['Status'] == True):
                    # conf_obj = add_TDF['conf_obj']
                    RobotLogger.log_logger.info("add_TDF file Details: %s" % add_TDF)
                else:
                    RobotLogger.log_logger.debug("Unable to add_TDF files Parameters")
                    return {'Status': False,
                            'Error': "Unable to add_TDF files parameters for the landslide test script"}
            #Add tdf file if TCP in traffic type
            if any("TCP" in item for item in traffic_list_upper):
                tdf_file_name = "tcp.csv"
                dataHeader = "Response Size, IP Segment Size"
                payloadSize = input_dict['trafficDetails']['payloadSize']
                segmentSize = input_dict['trafficDetails']['ueMaxIpSegmentSize']
                # payloadSize = 512
                data = dataHeader + "\n" + str(payloadSize) + "," + str(segmentSize)
                fileName = input_dict['logsPath'] + "/" + tdf_file_name
                RobotLogger.log_logger.debug("TDF File Name:%s" % (fileName))
                RobotLogger.log_logger.debug("TDF File Data:%s" % (data))
                try:
                    fh = open(fileName, "w+")
                    fh.write(data)
                    fh.close()
                except IOError:
                    RobotLogger.log_logger.debug("IOError occurred while creating tdf file.")
                except Exception as error:
                    print('Error: TDF File: File does not exists: {}'.format(error))
                # Add tdf file
                add_TDF = landslide_object.add_tdf(library_id, input_dict['logsPath'], tdf_file_name)

                if (add_TDF['Status'] == True):
                    # conf_obj = add_TDF['conf_obj']
                    RobotLogger.log_logger.info("add_TDF file Details: %s" % add_TDF)
                else:
                    RobotLogger.log_logger.debug("Unable to add_TDF files Parameters")
                    return {'Status': False,
                            'Error': "Unable to add_TDF files parameters for the landslide test script"}

            if any("PING" in item for item in traffic_list_upper):
                if input_dict['pingTraffic'] == "0":
                    remote_network_host_addr.append(input_dict['giEndPoint']['intranetIpPing'])
                elif input_dict['pingTraffic'] == "1":
                    remote_network_host_addr.append(input_dict['giEndPoint']['internetInfoPing'])
                elif input_dict['pingTraffic'] == "2":
                    remote_network_host_addr.append(input_dict['giEndPoint']['intranetIpPing'])
                    remote_network_host_addr.append(input_dict['giEndPoint']['internetInfoPing'])
            dmz_host_addr_remote = landslide_object.frame_multiple_network_hosts_parameters(
                conf_obj, "NetworkHostAddrRemote", remote_network_host_addr, node_index['gn_index'])
            if dmz_host_addr_remote['Status'] is True:
                conf_obj = dmz_host_addr_remote['conf_obj']
                RobotLogger.log_logger.info("DMZ Host details: %s" % dmz_host_addr_remote['conf_obj'])
            else:
                RobotLogger.log_logger.debug("Unable to Frame DMZ Parameters")
                return {'Status': False,
                        'Error': "Unable to configure dmz node parameters for the landslide test script"}

            # Framing DMF on SGW/PGW Nodal i.e Gn
            if "ENTERPRISE" not in input_dict['scenario']:
                ls_param = landslide_object.frame_dmf_parameters(conf_obj, "Dmf", library_id,
                                                                 traffic_list,
                                                                 [input_dict['dmz1Details'][
                                                                      'dmz1Ip']],
                                                                 node_index['gn_index'])
            else:
                ls_param = landslide_object.frame_dmf_parameters(conf_obj, "Dmf", library_id,
                                                                 traffic_list,
                                                                 remote_network_host_addr,
                                                                 node_index['gn_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
                RobotLogger.log_logger.info("dmf_node_param details: %s" % (ls_param))
            else:
                RobotLogger.log_logger.debug("Unable to Frame DMF Parameters")
                return {'Status': False,
                        'Error': "Unable to configure DMF node parameters for the landslide test script"}

            # Configure Traffic on Network Host
            if "ENTERPRISE" not in input_dict['scenario']:
                if home_addr_type == "3":
                    gi_param_dict = {'DataTraffic': 'Continuous', 'DualStackEn': 'true',
                                     'TrafficMtu': traffic_mtu}
                    RobotLogger.log_logger.debug("Home_addr_type is dual stack")
                else:
                    gi_param_dict = {'DataTraffic': 'Continuous', 'DualStackEn': 'false',
                                     'TrafficMtu': traffic_mtu}
                    RobotLogger.log_logger.debug("Home_addr_type is not dual stack")
                # Configure the Gi landslide parameters
                ls_param = landslide_object.frame_landslide_parameters(conf_obj, gi_param_dict,
                                                                       tc_name, tc_type,
                                                                       node_index['gi_index'])
                if ls_param['Status'] is True:
                    conf_obj = ls_param['conf_obj']
                    RobotLogger.log_logger.info("ls_param details: %s" % ls_param['conf_obj'])
                else:
                    RobotLogger.log_logger.debug("Unable to Frame Landslide Parameters")
                    return {'Status': False,
                            'Error': "Unable to configure gi parameters for the landslide test script"}

                dmz_node_param = self.configure_dmz_ip(
                    input_dict, landslide_object, node_index['gi_index'], conf_obj, home_addr_type)
                reserve_ports = reserve_ports + 1
                # dmz_port = input_dict['dmz1Details']['dmz1PhyName'].replace("v6", "")
                phy_eth_names_list.append(input_dict['dmz1Details'][
                                              'dmz1PhyName'].replace("v6", ""))
                if dmz_node_param['Status'] is True:
                    conf_obj = dmz_node_param['conf_obj']
                    RobotLogger.log_logger.info("dmz_node_param details: %s" % dmz_node_param['conf_obj'])
                else:
                    RobotLogger.log_logger.debug("Unable to Frame DMZ Parameters on Network Host")
                    return {'Status': False,
                            'Error': "Unable to configure dmz node parameters for the landslide test script"}

                gi_traffic_list = []
                for traffic in traffic_list:
                    if ("FTP" in traffic) or ("HTTP_Port" in traffic) or ("UDP" in traffic) or ("TCP" in traffic):
                        RobotLogger.log_logger.info("Traffic configuration: %s" % (traffic))
                        gi_traffic_list.append(traffic)

                if len(gi_traffic_list) >= 1:
                    ls_param = landslide_object.frame_dmf_parameters(conf_obj, "Dmf", library_id,
                                                                     gi_traffic_list,
                                                                     [input_dict['dmz1Details'][
                                                                          'dmz1Ip']],
                                                                     node_index['gi_index'])
                    if ls_param:
                        conf_obj = ls_param['conf_obj']
                        RobotLogger.log_logger.info("dmf_node_param details: %s" % (ls_param))
                    else:
                        RobotLogger.log_logger.debug("Unable to Frame DMF Parameters")
                        return {'Status': False,
                                'Error': "Unable to configure DMF node parameters for the landslide test script"}
        # Return the Value
        return {'Status': True, 'conf_obj': conf_obj, 'phy_eth_names_list': phy_eth_names_list}

    def plmn_change(self, input_parameter, landslide_object):
        """
        ######################################################################
            Title          : plmn_change()
            Description    : Configure Landslide configuration parameter for
                             PLMN_CHANGE
            Parameters     : input_parameter - TCL input parameter list as
                                string
                            landslide_object - Landslide object
            Return Value   : True - if test session configured successfully
                             False - if test session configured failed or
                             Exception while configuring test session
            Version  Author                 Date        Remarks
            0.1      Paulo Nicholas(pa685w) 09/18/2018  Initial Draft
            0.2      Paulo Nicholas(pa685w) 09/27/2018  Framed return value
                                            list and fixed integration issues
            0.3      Phanisree Y(py1780)    01/24/2019  [NIMB-7295]Add SUT if not available in landslide TAS
        ######################################################################
        """
        try:
            # Dictionary for integer to boolean conversion
            int_bool_dict = {"0": "false", "1": "true"}
            # Dictionary for RAT to integer conversion
            rat_int_dict = {"4G": "6", "3GS4": "1", "3GGn": "1"}
            # Dictionary for PDN to integer conversion
            pdn_int_dict = {"IPv4": "1", "IPv6": "2", "IPv4v6": "3"}
            # Convert list to dictionary
            util = UtilitiesLib()
            input_param = util.list_to_dict_inputparam(input_parameter)
            RobotLogger.log_logger.info("Landslide Input parameter dictionary: %s" % (input_param))
            home_address = pdn_int_dict[input_param['pdnType']]
            # Required variables
            test_server_name = input_param['chassis1Details']['testServer']
            library_name = input_param['ue1Details']['msisdn1']
            log_path = input_param['logsPath']
            conf_obj = ""
            tc_name = "GnConfigSimSGW"
            tc_type = "PGW Nodal"
            reserve_ports = 0
            phy_eth_names_list = []
            test_session_name = input_param['scenario']
            # if home_address == "3":
            #   test_session_name = test_session_name + "_IPv4v6"
            # Fetch library Id based on library name
            get_lib = landslide_object.get_library_details(library_name)
            if get_lib['Status'] is True:
                libraries = get_lib['Result']
                library_id = libraries['id']
            else:
                return {'Status': 'False', 'Error': "Failed to fetch library id"}
            # Get Test server details
            get_ts_details = landslide_object.get_test_servers(test_server_name)
            test_server_id = json.dumps(get_ts_details)
            if get_lib['Status'] is True:
                test_server_id = get_ts_details['ts_id']
            else:
                return {'Status': 'False', 'Error': "Failed to get test server details"}
            # Get test script
            json_obj = landslide_object.get_test_script_json(library_id,
                                                             test_session_name)
            if json_obj['Status'] is True:
                tc_script_json = json_obj['json_res']
            else:
                return {'Status': 'False', 'Error': "Failed to get test session JSON"}
            # Get test instances for nodes Gn, AF, mog
            tc_inst = landslide_object.get_tc_inst(tc_script_json)
            if tc_inst['Status'] is True:
                node_index = tc_inst['tc_inst_dict']
            else:
                return {'Status': 'False', 'Error': "Failed to get test session index information"}
            # Framing Test Session Details for Landslide Test Session
            ts_param = landslide_object.frame_test_session_parameters(
                conf_obj, node_index['total_tc_inst'], library_id,
                test_server_name, test_session_name)
            if ts_param['Status'] is True:
                conf_obj = ts_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "Failed to frame basic landslide test session parameters"}
            # Framing Gn parameters
            gn_param_dict = {'Gtp2IncTaiEn': 'true',
                             'TgtGtp2IncModServNetw': "true",
                             'Gtp2IncRaiEn': 'false',
                             'TgtGtp2IncTaiEn': "true",
                             'Gtp2IncEcgiEn': 'true',
                             'MobilityMode': 'Continuous Handoff',
                             'Gtp2N3Attempts': "5",
                             'Gtp2ApnTotalApns_0': "1",
                             'Gtp2ApnNumSpecifiedApns_0': "0",
                             'Gtp2IncCgiEn': 'false', 'Gtp2T3Time': "3",
                             'S5Protocol': 'GTPv2', 'TestActivity': 'Mobility',
                             'NetworkHostNatedTrafficEn': "true",
                             'TgtGtp2IncEcgiEn': "true",
                             'Gtp2IncSaiEn': 'false', 'NtwkInterface': 'S5-S8',
                             'TgtGtp2IncModUli': 'true',
                             'TgtGtp2IncSaiEn': 'false',
                             'TgtGtp2IncCgiEn': 'false',
                             'TgtGtp2IncRaiEn': 'false',
                             'SessionRetries': 'false',
                             "HomeAddrType": home_address,
                             "Gtp2Imei": input_param['imei'],
                             "Gtp2Imsi": input_param['ue1Details']['imsi1'],
                             "Gtp2MsIsdn": input_param[
                                 'ue1Details']['msisdn1'],
                             "Gtp2RadioAccessType": rat_int_dict[
                                 input_param['callType']],
                             "Gtp2Mcc": input_param['sgw1Details']['mcc1'],
                             "Gtp2Mnc": input_param['sgw1Details']['mnc1'],
                             "Gtp2Tac": input_param['sgw1Details']['tac1'],
                             "Gtp2Ecgi": input_param['sgw1Details'][
                                 'eCellId1'],
                             "Gtp2AmbrDownlink": input_param[
                                 'apn1Details']['apn1DownlinkAmbr'],
                             "Gtp2AmbrUplink": input_param[
                                 'apn1Details']['apn1UplinkAmbr'],
                             "Gtp2Apn_0": input_param[
                                 'apn1Details']['apn1Name'],
                             "Gtp2QosClassId_1": input_param[
                                 'apn1Details']['apn1Qci'],
                             "Gtp2QosArpValue_1": input_param[
                                 'apn1Details']['apn1Pl'],
                             "Gtp2QosArpPreemptCapEn_1": int_bool_dict[
                                 input_param['apn1Details']['apn1Pci']],
                             "Gtp2QosArpPreemptVulnEn_1": int_bool_dict[
                                 input_param['apn1Details']['apn1Pvi']],
                             "MobilityTimeMs": str(int(input_param['mobilityTimeline1Details'][
                                                           'mobilityInterval']) * 1000),
                             "TgtGtp2Mcc": input_param['sgw2Details']['mcc2'],
                             "TgtGtp2Mnc": input_param['sgw2Details']['mnc2'],
                             "TgtGtp2Tac": input_param['sgw2Details']['tac2'],
                             "TgtGtp2Ecgi": input_param['sgw2Details']['eCellId2']}
            # Create PgwSut dictionary and assign in gn_param_dict
            pgw1_ip = input_param['gw1Details']['pgw1Ip']
            pgw1_ip = pgw1_ip.replace(".", "_")
            gn_param_dict['PgwSut'] = pgw1_ip
            pgw_sut = landslide_object.add_sut(input_param['gw1Details']['pgw1Ip'],
                                               input_param['gw1Details']['pgw1Ip'],
                                               pgw1_ip)
            if pgw_sut['Status'] is True:
                RobotLogger.log_logger.info("Created pgw SUT Object: %s" % (conf_obj))
            else:
                return {'Status': False,
                        'Error': "Unable to Create PGW sut parameters for the landslide test script"}
            RobotLogger.log_logger.info("Landslide Gn Parameters: %s" % (gn_param_dict))
            # Configure the Gn landslide parameters
            ls_param = landslide_object.frame_landslide_parameters(
                conf_obj, gn_param_dict, tc_name, tc_type,
                node_index['gn_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_landslide_parameters failed"}
            # Framing PGW sut details for Landslide Test Session
            pgw_param = landslide_object.frame_sut_parameters(
                conf_obj, "PgwSut", pgw1_ip, node_index['gn_index'])
            if pgw_param['Status'] is True:
                conf_obj = pgw_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_sut_parameters failed"}
            # Framing Sgw control address for Landslide Test Session
            node_name = "SgwControlAddr"
            node_ip = input_param['sgw1Details']['sgw1Ip']
            next_hop_ip = input_param['sgw1Details']['sgw1GwIp']
            num_link_nodes = "1"
            phy_eth = input_param['sgw1Details']['sgw1PhyName']
            mtu = 1500
            forced_eth = input_param['sgw1Details']['sgw1PhyName']
            vlan_id = 0
            sgw_node_config = landslide_object.frame_node_parameters(
                conf_obj, node_name, node_ip, next_hop_ip, num_link_nodes,
                phy_eth, mtu, forced_eth, vlan_id, node_index['gn_index'])
            if sgw_node_config['Status'] is True:
                conf_obj = sgw_node_config['conf_obj']
                reserve_ports = reserve_ports + 1
                phy_eth_names_list.append(phy_eth)
            else:
                return {'Status': 'False', 'Error': "SGW frame_node_parameters failed"}
            # Framing Mob SGW address for Landslide Test Session
            node_name = "MobSgwControlAddr"
            node_ip = input_param['sgw2Details']['sgw2Ip']
            next_hop_ip = input_param['sgw2Details']['sgw2GwIp']
            num_link_nodes = "1"
            phy_eth = input_param['sgw2Details']['sgw2PhyName']
            mtu = 1500
            forced_eth = input_param['sgw2Details']['sgw2PhyName']
            vlan_id = 0
            mob_node_config = landslide_object.frame_node_parameters(
                conf_obj, node_name, node_ip, next_hop_ip, num_link_nodes,
                phy_eth, mtu, forced_eth, vlan_id, node_index['gn_index'])
            if mob_node_config['Status'] is True:
                conf_obj = mob_node_config['conf_obj']
            else:
                return {'Status': 'False', 'Error': "Mob SGW frame_node_parameters failed"}
            # Framing Dmz node parameters
            if home_address == "3":
                dmz_v4_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "Ipv4NetworkHostAddrLocal",
                    input_param['dmz1Details']['dmz1Ip'],
                    input_param['dmz1Details']['dmz1GwIp'], "1",
                    input_param['dmz1Details']['dmz1PhyName'], 1500,
                    "", input_param['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_v4_node_param['Status'] is True:
                    conf_obj = dmz_v4_node_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "DMZv6 frame_node_parameters failed"}
                dmz_v6_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "Ipv6NetworkHostAddrLocal",
                    input_param['dmz1Details']['dmz1Ipv6'],
                    input_param['dmz1Details']['dmz1GwIpv6'], "1",
                    input_param['dmz1Details']['dmz1PhyNamev6'], 1500,
                    "", input_param['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_v6_node_param['Status'] is True:
                    conf_obj = dmz_v6_node_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "DMZv6 frame_node_parameters failed"}
            else:
                dmz_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "NetworkHostAddrLocal",
                    input_param['dmz1Details']['dmz1Ip'],
                    input_param['dmz1Details']['dmz1GwIp'], "1",
                    input_param['dmz1Details']['dmz1PhyName'], 1500,
                    "", input_param['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_node_param['Status'] is True:
                    conf_obj = dmz_node_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "DMZ frame_node_parameters failed"}
            reserve_ports = reserve_ports + 1
            dmz_port = input_param['dmz1Details']['dmz1PhyName']
            phy_eth_names_list.append(dmz_port)
            # Enable port capture
            pc_param = landslide_object.frame_port_capture_parameters(
                conf_obj, reserve_ports, phy_eth_names_list, test_server_id,
                on_start=True)
            if pc_param['Status'] is True:
                conf_obj = pc_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_port_capture_parameters failed"}
            # Apply and Save the configuration
            conf_test_session = landslide_object.config_landslide_test_session(
                conf_obj, library_id, test_session_name)
            if conf_test_session['Status'] is True:
                delay_step = "2"
                # phy_list_str = ' '.join(phy_eth_names_list)
                return {'Status': 'True', 'Info': "Successfully Configured", 'trafficParameterList': "lib_id " + str(
                    library_id) + " tsname " + test_server_name + " delaystep " + delay_step + " logfilepath " + log_path + " dmz_port " + dmz_port + " gn_port " + phy_eth + " home_address " + home_address}
            else:
                return {'Status': 'False', 'Error': "Configuration failed"}
        except TypeError:
            RobotLogger.log_logger.debug(
                "TypeError occurred while configure plmn_change:%s" % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "TypeError occurred while configure plmn_change"}
        except ValueError:
            RobotLogger.log_logger.debug(
                "OSError occurred while configure plmn_change:%s " % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "OSError occurred while configure plmn_change"}
        except IOError:
            RobotLogger.log_logger.debug(
                "IOError occurred while configure plmn_change:%s " % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "IOError occurred while configure plmn_change"}
        except Exception:
            RobotLogger.log_logger.debug(
                "Exception occurred while configure plmn_change:%s" % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "Exception occurred while configure plmn_change"}

    def ir92_ir94_ipme(self, input_parameter, landslide_object):
        """
            ######################################################################
                Title          :ir92_ir94_ipme()
                Description    : Configure Landslide configuration parameter for IR92_IR94_IPME
                Parameters     :input_parameter - TCL input parameter list as string
                                landslide_object - Landslide object
                Return Value   : Configured test Session - Configured test session
                                 False - Exception while framing landslide config param
                Version  Author                 Date        Remarks
                0.1     Phanisree Y(py1780) 09/17/2018  Initial Draft
                0.2     Phanisree Y(py1780) 10/Oct/2018 Enhanced the procedure to invoke congigureDRA
                        method to configure MOG
                0.3     Phanisree y (py1780) 01/24/2019 [NIMB-7295]Add SUT if not available in landslide TAS
            ######################################################################
        """

        try:
            # Dictionary for integer to boolean conversion
            int_bool_dict = {"0": "false", "1": "true"}
            # Dictionary for RAT to integer conversion
            rat_int_dict = {"4G": "6", "3G-S4": "1", "3GGN": "1"}
            # Dictionary for PDN to integer conversion
            pdn_int_dict = {"ipv4": "1", "ipv6": "2", "ipv4v6": "3"}
            # convert list to dictionary --- method invoke from utilities.py
            RobotLogger.log_logger.info("Input parameter dictionary: %s" % (input_parameter))
            util = UtilitiesLib()
            input_dict = util.list_to_dict_inputparam(input_parameter)
            RobotLogger.log_logger.info("Landslide Input parameter dictionary: %s" % (input_dict))
            # Required variables
            reserve_ports = 0
            phy_eth_names_list = []
            test_server_name = input_dict['chassisDetails']['testServer']
            RobotLogger.log_logger.info("Test server name: %s" % (test_server_name))
            library_name = input_dict['ue1Details']['msisdn1']
            test_session_name = input_dict['scenario']
            log_path = input_dict['logsPath']
            gn_port = input_dict['chassisDetails']['gnPort']
            dmz_port = "{}"
            gi_port = "{}"
            mog_port = "{}"
            rx_port = "{}"
            conf_obj = ""
            tc_name = ""
            tc_type = ""
            # Fetch library Id based on library name
            get_lib = landslide_object.get_library_details(library_name)
            if get_lib['Status'] is True:
                # library_id = get_lib["id"]
                library_id = get_lib['Result']['id']
                RobotLogger.log_logger.info("Library Id: %s" % (library_id))
            else:
                return {'Status': 'False', 'Error': "Unable to retrieve library id for the landslide test script"}
            # Get Test server details
            get_ts_details = landslide_object.get_test_servers(test_server_name)
            if get_lib['Status'] is True:
                ts_id = get_ts_details["ts_id"]
                RobotLogger.log_logger.info("Test server details: %s" % (ts_id))
            else:
                return {'Status': 'False', 'Error': "Unable to retrieve test server id for the landslide test script"}
            # Get test script
            json_obj = landslide_object.get_test_script_json(library_id, test_session_name)
            if json_obj['Status'] is True:
                tc_script_json = json_obj['json_res']
            else:
                return {'Status': 'False', 'Error': "Unable to get json object for the landslide test script"}
            # Set test instances for nodes Gn, AF, mog
            tc_inst = landslide_object.get_tc_inst(tc_script_json)
            if tc_inst['Status'] is True:
                node_index = tc_inst['tc_inst_dict']
                RobotLogger.log_logger.info("Node Index details: %s" % (node_index))
            else:
                RobotLogger.log_logger.debug("Unable to frame node index details")
                return {'Status': 'False',
                        'Error': "Unable to get node instance indexes  for the landslide test script"}

            # Frame Gn Node parameters
            gn_param_dict = {}
            pdp_type = input_dict['ue1Details']['ue1IpType'].lower()
            home_addr_type = pdn_int_dict[pdp_type]
            # set radio access type from call type
            rat_type = input_dict['callType'].upper()
            radio_access_type = rat_int_dict[rat_type]
            # set pci and pvi values
            RobotLogger.log_logger.info("PCI Initial: %s" % (input_dict['apn1Details']['apn1Pci']))
            RobotLogger.log_logger.info("PVI Initial: %s" % (input_dict['apn1Details']['apn1Pvi']))
            input_dict['apn1Details']['apn1Pci'] = int_bool_dict[input_dict[
                'apn1Details']['apn1Pci']]
            input_dict['apn1Details']['apn1Pvi'] = int_bool_dict[input_dict[
                'apn1Details']['apn1Pvi']]

            RobotLogger.log_logger.info("PCI After: %s" % (input_dict['apn1Details']['apn1Pci']))
            RobotLogger.log_logger.info("PVI After: %s" % (input_dict['apn1Details']['apn1Pvi']))
            if "QPP_IMS" in input_dict['scenario']:
                input_dict['Gtp2CustomMsgEn'] = "true"
            else:
                input_dict['Gtp2CustomMsgEn'] = "false"

            if input_dict['callType'] == "4G":
                mcc = input_dict['enodeB1Details']['mcc1']
                mnc = input_dict['enodeB1Details']['mnc1']
                tac = input_dict['enodeB1Details']['tac1']
                cellid = input_dict['enodeB1Details']['eCellId1']
            elif input_dict['callType'] == "3G-S4":
                mcc = input_dict['rncDetails']['mcc1']
                mnc = input_dict['rncDetails']['mnc1']
                tac = input_dict['rncDetails']['tac1']
                cellid = input_dict['rncDetails']['eCellId1']
            gn_param_dict = {'Gtp2Imsi': input_dict['ue1Details']['imsi1'],
                             'Gtp2Imei': input_dict['ue1Details']['mei1'],
                             'Gtp2MsIsdn': input_dict['ue1Details']['msisdn1'],
                             'Gtp2RadioAccessType': radio_access_type,
                             'Gtp2Mcc': mcc,
                             'Gtp2Mnc': mnc,
                             'SessionRetries': 'false',
                             'Gtp2T3Time': '3', 'Gtp2N3Attempts': '5',
                             'Gtp2CustomMsgEn': input_dict['Gtp2CustomMsgEn'],
                             'HomeAddrType': home_addr_type,
                             'Gtp2AmbrDownlink': input_dict['apn1Details']['apn1DownlinkAmbr'],
                             'Gtp2AmbrUplink': input_dict['apn1Details']['apn1UplinkAmbr'],
                             'Gtp2QosClassId_1': input_dict['apn1Details']['apn1Qci'],
                             'Gtp2QosArpValue_1': input_dict['apn1Details']['apn1Pl'],
                             'Gtp2QosArpPreemptCapEn_1': input_dict['apn1Details']['apn1Pci'],
                             'Gtp2QosArpPreemptVulnEn_1': input_dict['apn1Details']['apn1Pvi'],
                             'Gtp2Apn_0': input_dict['apn1Details']['apn1Name'],
                             'Gtp2IncTaiEn': 'true',
                             'Gtp2IncEcgiEn': 'true',
                             'Gtp2Tac': tac,
                             'Gtp2Ecgi': cellid,
                             'Gtp2IncSaiEn': 'false', 'Gtp2IncRaiEn': 'false',
                             'Gtp2IncCgiEn': 'false',
                             'VolteEn': 'true',
                             'DataTraffic': 'Disabled', 'Gtp2UliDbCmdCbRspEn': 'true',
                             'UeRtpAudioPort': 6000,
                             'UeRtpVideoPort': 7000, 'UeMsrpPort': 2855, 'UeRttPort': 8000,
                             'ImsNodeIpAddr': input_dict['sipDetails']['sipIp'],
                             'ImsNodePort': '5060',
                             'S5Protocol': 'GTPv2', 'ImsNodeType': 'Remote',
                             'ImsNodePcscfAddrType': '0',
                             'SipTransport': 'UDP',
                             'SipMaxMsgBufferSize': '2048'}

            if "REGISTRATION" in input_dict['scenario']:
                dial_plan_usr = "#(" + input_dict["dialPlanUser"] + ")"
                temp_dict = {'ServingNode': 'MME', 'UePattern': '2',
                             'ImsSipSubsPublicUserName': dial_plan_usr,
                             'ImsSipSubsPrivateUserName': dial_plan_usr,
                             'SipCallSetupEn': 'false',
                             'UeAuthenticationEn': 'false'}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
            else:
                temp_dict = {'SipCallSetupEn': 'true', 'SipSubscriberUriScheme': '0',
                             'SipEndpointUriScheme': '0',
                             'UeCallStart': '1'}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
                if not "MT_Early_Media" in input_dict['scenario']:
                    temp_dict = {'UeCallPending': 1000, 'UeCallLength': input_dict['audioDuration']}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict

            if "IPME_3G" in input_dict['scenario']:
                temp_dict = {'ServingNode': 'SGSN', 'UeCallLength': input_dict['audioDuration'],
                             'MsrpEn': 'true',
                             'UePattern': '2', 'RtpTrafficEn': 'false'}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
            if "IPME_N" in input_dict['scenario']:
                temp_dict = {'ServingNode': 'MME', 'UeCallLength': input_dict['audioDuration'],
                             'MsrpEn': 'true',
                             'UePattern': '2', 'RtpTrafficEn': 'false'}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict

            if ("IR92" in input_dict['scenario']) or ("SOS" in input_dict['scenario']) or (
                    "QPP_IR9" in input_dict['scenario']):
                temp_dict = {'RtpTrafficEn': 'true', 'UeAuthenticationEn': 'true',
                             'RtpDmf1Type': 'Audio',
                             'RtpTrafficStartDelay': '1000', 'ServingNode': 'MME'}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
                if "MT_Early_Media" in input_dict['scenario']:
                    temp_dict = {'UePattern': 3}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
                else:
                    temp_dict = {'UeCallLength': input_dict['audioDuration'], "UePattern": 2}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
                if "RTT" in input_dict['scenario']:
                    temp_dict = {"RtpDmf2Type": "RTT", "DedicatedsPerDefaultBearer": 2}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
                if "IPME" in input_dict['scenario']:
                    temp_dict = {"DedicatedsPerDefaultBearer": 2, "MsrpEn": True}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
                if "upgrade" in input_dict['scenario']:
                    temp_dict = {"UeVideoDelay": input_dict['videoTimer'], "UeAudioDelay": 0}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
            elif "IR94" in input_dict['scenario']:
                temp_dict = {"RtpTrafficEn": True, "UeAuthenticationEn": True,
                             "RtpDmf1Type": "Audio",
                             "RtpTrafficStartDelay": 1000, "UeVideoDelay": 0,
                             "UeReleaseMode": "Normal",
                             "RtpDmf2Type": "Video", "ServingNode": "MME", "UePattern": 2}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
                if "IPME" in input_dict['scenario']:
                    temp_dict = {"DedicatedsPerDefaultBearer": 3, "MsrpEn": True}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
                if "downgrade" in input_dict['scenario']:
                    temp_dict = {"UeVideoDelay": 0, "UeReleaseMode": "VideoFirst",
                                 "UeVideoDuration": input_dict['videoTimer']}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
            if input_dict['qppNegativeFlag'] is True:
                gn_param_dict["Gtp2CustomMsgEn"] = True

            # Framing Test Session Details for Landslide Test Session
            ts_param = landslide_object.frame_test_session_parameters(
                conf_obj, node_index['total_tc_inst'], library_id, test_server_name,
                test_session_name)
            if ts_param['Status'] is True:
                conf_obj = ts_param['conf_obj']
                RobotLogger.log_logger.info("Initial Config Object: %s" % (conf_obj))
            else:
                RobotLogger.log_logger.debug("Could not frame test server details")
                return {'Status': 'False',
                        'Error': "Unable to frame test session parameters for the landslide test script"}

            # Configure the Gn landslide parameters
            ls_param = landslide_object.frame_landslide_parameters(conf_obj, gn_param_dict,
                                                                   tc_name, tc_type,
                                                                   node_index['gn_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
                RobotLogger.log_logger.info("Gn Config Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure gn node parameters for the landslide test script"}

            # Framing SGW sut details for Landslide Test Session
            sgw1_ip = input_dict['gw1Details']['sgw1Ip']
            sgw1_ip = sgw1_ip.replace(".", "_")
            sgw_sut_param = landslide_object.add_sut(input_dict['gw1Details']['sgw1Ip'],
                                                     input_dict['gw1Details']['sgw1Ip'], sgw1_ip)
            if sgw_sut_param['Status'] is True:
                # conf_obj = sgw_sut_param['conf_obj']
                RobotLogger.log_logger.info("Created SGW SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to Create sgw sut parameters for the landslide test script"}
            # Framing SGW sut details for Landslide Test Session
            sgw_param = landslide_object.frame_sut_parameters(conf_obj, "SgwSut", sgw1_ip,
                                                              node_index['gn_index'])
            if sgw_param['Status'] is True:
                conf_obj = sgw_param['conf_obj']
                RobotLogger.log_logger.info("Config SGW SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure sgw sut parameters for the landslide test script"}

            # Framing SGW User sut details for Landslide Test Session
            sgw1user_ip = input_dict['gw1Details']['sgw1S1uIp']
            sgw1user_ip = sgw1user_ip.replace(".", "_")
            sgw_user_sut_param = landslide_object.add_sut(input_dict['gw1Details']['sgw1S1uIp'],
                                                     input_dict['gw1Details']['sgw1S1uIp'], sgw1user_ip)
            if sgw_user_sut_param['Status'] is True:
                # conf_obj = sgw_sut_param['conf_obj']
                RobotLogger.log_logger.info("Created SGW USER SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to Create sgw  user sut parameters for the landslide test script"}

            sgw_param = landslide_object.frame_sut_parameters(conf_obj, "SgwUserSut", sgw1user_ip,
                                                              node_index['gn_index'])
            if sgw_param['Status'] is True:
                conf_obj = sgw_param['conf_obj']
                RobotLogger.log_logger.info("Config SGW User SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure sgw user sut parameters for the landslide test script"}

            # Framing PGW sut details for Landslide Test Session
            pgw1_ip = input_dict['gw1Details']['pgw1Ip']
            pgw1_ip = pgw1_ip.replace(".", "_")
            pgw_sut_param = landslide_object.add_sut(input_dict['gw1Details']['pgw1Ip'],
                                                     input_dict['gw1Details']['pgw1Ip'], pgw1_ip)
            if pgw_sut_param['Status'] is True:
                # conf_obj = sgw_sut_param['conf_obj']
                RobotLogger.log_logger.info("Created PGW SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to Create PGW sut parameters for the landslide test script"}

            pgw_param = landslide_object.frame_sut_parameters(conf_obj, "PgwV4Sut", pgw1_ip,
                                                              node_index['gn_index'])
            if pgw_param['Status'] is True:
                conf_obj = pgw_param['conf_obj']
                RobotLogger.log_logger.info("Config PGW SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure pgw sut parameters for the landslide test script"}
            if input_dict['callType'] == "4G":
                # Framing enodeB control address for Landslide Test Session
                enodeb_node_param = landslide_object.frame_node_parameters(conf_obj, "EnbUserAddr",
                                                                           input_dict[
                                                                               'enodeB1Details'][
                                                                               'enodeB1Ip'],
                                                                           input_dict[
                                                                               'enodeB1Details'][
                                                                               'enodeB1GwIp'],
                                                                           1,
                                                                           input_dict[
                                                                               'enodeB1Details'][
                                                                               'enodeB1PhyName'],
                                                                           1500, "",
                                                                           input_dict[
                                                                               'chassisDetails'][
                                                                               'gnVlan'],
                                                                           node_index['gn_index'])
                reserve_ports = reserve_ports + 1
                phy_eth_names_list.append(input_dict['enodeB1Details'][
                                              'enodeB1PhyName'].replace("v6", ""))
                RobotLogger.log_logger.info("Config enodeB details: %s" % (conf_obj))
                if enodeb_node_param['Status'] is True:
                    conf_obj = enodeb_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config enodeB details: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure enodeB node parameters for the landslide test script"}

                # Framing MMEcontrol address for Landslide Test Session
                mme_node_param = landslide_object.frame_node_parameters(conf_obj, "MmeControlAddr",
                                                                        input_dict['mme1Details'][
                                                                            'mme1Ip'],
                                                                        input_dict['mme1Details'][
                                                                            'mme1GwIp'], 1,
                                                                        input_dict['mme1Details'][
                                                                            'mme1PhyName'], 1500,
                                                                        input_dict[
                                                                            'mme1Details'][
                                                                            'mme1PhyName'],
                                                                        input_dict[
                                                                            'chassisDetails'][
                                                                            'giVlan'],
                                                                        node_index['gn_index'])
                if mme_node_param['Status'] is True:
                    conf_obj = mme_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config mme details: %s" % (conf_obj))
                    RobotLogger.log_logger.info("Gn Parameters framed successfully")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure mme node parameters for the landslide test script"}
            elif input_dict['callType'] == "3G-S4":
                # Framing RNC control address for Landslide Test Session
                '''rnc_node_param = landslide_object.frame_node_parameters(conf_obj, "SgsnUsrAddr",
                                                                       input_dict['rncDetails'][
                                                                       'rnc1Ip'],
                                                                       input_dict['rncDetails'][
                                                                       'rnc1GwIp'], 1,
                                                                       input_dict['rncDetails'][
                                                                       'rnc1PhyName'], 1500,
                                                                       input_dict['rncDetails'][
                                                                       'rnc1PhyName'],
                                                                       input_dict['chassisDetails'][
                                                                       'gnVlan'],
                                                                       node_index['gn_index'])
                if rnc_node_param['Status'] is True:
                    conf_obj = rnc_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config rnc details: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                'Error': "Unable to configure rnc node parameters for the landslide test script"}
                '''
                # Framing SGSN address for Landslide Test Session
                sgsn_node_param = landslide_object.frame_node_parameters(conf_obj, "SgsnCtlAddr",
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1Ip'],
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1GwIp'], 1,
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1PhyName'], 1500,
                                                                         input_dict[
                                                                             'sgsnDetails'][
                                                                             'sgsn1PhyName'],
                                                                         input_dict[
                                                                             'chassisDetails'][
                                                                             'gnVlan'],
                                                                         node_index['gn_index'])
                reserve_ports = reserve_ports + 1
                phy_eth_names_list.append(input_dict['sgsnDetails'][
                                              'sgsn1PhyName'].replace("v6", ""))
                if sgsn_node_param['Status'] is True:
                    conf_obj = sgsn_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config sgsn details: %s" % (conf_obj))
                    RobotLogger.log_logger.info("Gn Parameters framed successfully")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure sgsn node parameters for the landslide test script"}

            # Framing IMS node parameters
            ims_param_dict = {'TxClnSutPrimaryHost': '*.' + input_dict['diameterDetails'][
                'destinationRealm'],
                              'TxClnSutPrimaryRealm': input_dict['diameterDetails'][
                                  'destinationRealm'],
                              'TxClnSutPort': input_dict['diameterDetails']['destinationHost'],
                              'TxClnOriginHost': input_dict['RxDetails']['originHost'],
                              'TxClnOriginRealm': input_dict['RxDetails']['originRealm'],
                              'SipSubscriberUriScheme': '0', 'SipEndpointUriScheme': '1',
                              'CommandMode': 'Off',
                              'ImsMode': 'Endpoint', 'ImsApn': input_dict['apn1Details']['apn1Name'],
                              'ImsInterface': 'Gm', 'RxEn': 'true', 'SipRegExpires': '600000',
                              'NumUes': input_dict['ue1Details']['ueCount'],
                              'SipSubscribersPerUe': input_dict['ue1Details']['ueCount'],
                              'PCRFClnCcMsisdnEn': 'true',
                              'PCRFClnCcMsisdn': input_dict['ue1Details']['msisdn1'],
                              'ImsNodeStartingRtpAudioPort': 6000,
                              'ImsNodeStartingRtpVideoPort': 7000, 'ImsNodeStartingMsrpPort': 2855,
                              'ImsNodeStartingRttPort': 8000, 'ImsNodeCallStart': '1',
                              'SipTransport': 'UDP',
                              'SipMaxMsgBufferSize': '2048', 'TxClnConfigMcdEn': 'true'}

            if (("WO_NETLOC" in input_dict['scenario']) or ("REGISTRATION " in input_dict[
                'scenario'])):
                ims_param_dict['ImsNodeNetLocEn'] = "false"
            else:
                ims_param_dict['ImsNodeNetLocEn'] = "true"
            if (("IR9" in input_dict['scenario']) or ("REGISTRATION" in input_dict['scenario'])):
                temp_dict = {'TxClnCodecEn_0': 'true', 'TxClnNumCodecs_0': '2',
                             'TxClnAFAppIdent_0': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                             'TxClnMaxReqUL_0': '38000',
                             'TxClnMaxReqDL_0': '38000', 'TxClnRRBandwidth_0': '1425',
                             'TxClnRSBandwidth_0': '475',
                             'TxClnFlowStatus_0': '2', 'RtpTrafficEn': 'true',
                             'RtpDmf1Type': 'Audio',
                             'RtpTrafficStartDelay': '1000'}
                ims_param_dict = {**ims_param_dict, **temp_dict}
                del temp_dict
                if "MT_Early_Media" in input_dict['scenario']:
                    temp_dict = {'ImsNodeCallPending': '1000',
                                 'ImsNodeCallLength': 'simulator/audioDuration'}
                    ims_param_dict = {**ims_param_dict, **temp_dict}
                    del temp_dict
                if "REGISTRATION" in input_dict['scenario']:
                    temp_dict = {'ImsSrvProfilePublicUserName': dial_plan_usr,
                                 'ImsSrvProfilePrivateUserName': dial_plan_usr}
                    ims_param_dict = {**ims_param_dict, **temp_dict}
                    del temp_dict
                if "IR94" in input_dict['scenario']:
                    temp_dict = {'RtpDmf2Type': 'Video', 'TxClnCodecEn_1': 'true',
                                 'TxClnNumCodecs_1': '2',
                                 'TxClnAFAppIdent_1': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                                 'TxClnMaxReqUL_1': '38000',
                                 'TxClnMaxReqDL_1': '38000', 'TxClnRRBandwidth_1': '1425',
                                 'TxClnRSBandwidth_1': '475',
                                 'TxClnFlowStatus_1': '2', 'SipRegEn': 'true',
                                 'ImsNodeFunctionalityPattern': '3'}
                    ims_param_dict = {**ims_param_dict, **temp_dict}
                    del temp_dict
                    if "downgrade" in input_dict['scenario']:
                        temp_dict = {'UeVideoDelay': '0', 'UeReleaseMode': 'VideoFirst',
                                     'UeVideoDuration': 'simulator/videoTimer'}
                        ims_param_dict = {**ims_param_dict, **temp_dict}
                        del temp_dict
                if "EMERGENCY" in input_dict['scenario']:
                    ims_param_dict['EmergencyEn'] = True
                if "IPME" in input_dict['scenario']:
                    temp_dict = {'TxClnAFAppIdent_2': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                                 'TxClnMaxReqUL_2': '1024000',
                                 'TxClnMaxReqDL_2': '1024000', 'TxClnFlowStatus_2': '2',
                                 'MsrpSendMessagesEn': 'true',
                                 'MsrpStartDelay': '1000', 'MsrpInterval': '1000',
                                 'MsrpEn': 'true',
                                 'TxClnMaxReqUL_3': '330', 'TxClnMaxReqDL_3': '330'}
                    ims_param_dict = {**ims_param_dict, **temp_dict}
                    del temp_dict
                if "RTT" in input_dict['scenario']:
                    temp_dict = {'RtpDmf2Type': 'RTT', 'TxClnCodecEn_3': 'true',
                                 'TxClnNumCodecs_3': '2',
                                 'TxClnAFAppIdent_3': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                                 'TxClnMaxReqUL_3': '38000',
                                 'TxClnMaxReqDL_3': '38000', 'TxClnRRBandwidth_3': '1425',
                                 'TxClnRSBandwidth_3': '475',
                                 'TxClnFlowStatus_3': '2', 'SipRegEn': 'true'}
                    ims_param_dict = {**ims_param_dict, **temp_dict}
                    del temp_dict

            elif "IPME" in input_dict['scenario']:
                temp_dict = {'TxClnAFAppIdent_2': 'urn:urn-7:3gpp-service.ims.icsi.mmtel',
                             'TxClnMaxReqUL_2': '1024000',
                             'TxClnMaxReqDL_2': '1024000', 'TxClnFlowStatus_2': '2',
                             'MsrpSendMessagesEn': 'true',
                             'MsrpStartDelay': '1000', 'MsrpInterval': '1000',
                             'SipRegEn': 'true', 'MsrpEn': 'true',
                             'ImsNodeFunctionalityPattern': '3'}
                ims_param_dict = {**ims_param_dict, **temp_dict}
                del temp_dict

            # Configure the ims node landslide parameters
            ls_param = landslide_object.frame_landslide_parameters(conf_obj, ims_param_dict,
                                                                   tc_name, tc_type,
                                                                   node_index['ims_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
                RobotLogger.log_logger.info("Config ims_node parameters: %s" % (conf_obj))
            else:
                RobotLogger.log_logger.info("Unable to configure ims node parameters: %s" % ims_param_dict)
                return {'Status': 'False', 'Error': "Unable to configure af parameters for the landslide test script"}

            # Framing TxClnSutPrimarySrv sut details for Landslide Test Session
            diameter_ip = input_dict["diameterDetails"]["diameterIp"]
            diameter_ip = diameter_ip.replace(":", "_")
            ims_sut = landslide_object.add_sut(input_dict["diameterDetails"]["diameterIp"],
                                               input_dict["diameterDetails"]["diameterIp"],
                                               diameter_ip)
            if ims_sut['Status'] is True:
                # conf_obj = sgw_sut_param['conf_obj']
                RobotLogger.log_logger.info("Created IMS SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to Create IMS sut parameters for the landslide test script"}

            ims_sut_param = landslide_object.frame_sut_parameters(conf_obj, "TxClnSutPrimarySrv",
                                                                  diameter_ip,
                                                                  node_index['ims_index'])
            if ims_sut_param['Status'] is True:
                conf_obj = ims_sut_param['conf_obj']
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure volte sut parameters for the landslide test script"}

            # Frame and modify avp parameters
            if re.search("SOS", input_dict['apn1Details']['apn1Name'], re.IGNORECASE):
                avp_dict = {"Service-URN": input_dict['serviceURN']}
                sos_avp_config = landslide_object.frame_avp_parameters(conf_obj, avp_dict,
                                                                       "TxClnVsa",
                                                                       node_index['ims_index'],
                                                                       tc_script_json)
                if sos_avp_config['Status'] is True:
                    conf_obj = sos_avp_config['conf_obj']
                    RobotLogger.log_logger.info("Sos Parameters framed successfully")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to modify and configure avp parameters for sos apn in the landslide test script"}

            # Frame node parameters
            sip_outbound_port = input_dict['sipDetails']['sipPort'].replace("v6", "")
            dmz_port = sip_outbound_port
            af_outbound_port = input_dict['RxDetails']['RxPort'].replace("v6", "")
            rx_port = af_outbound_port
            sip_node_param = landslide_object.frame_node_parameters(conf_obj, "SipPCSCFAddr",
                                                                    input_dict['sipDetails'][
                                                                        'sipIp'],
                                                                    input_dict['sipDetails'][
                                                                        'sipGwIp'], 1,
                                                                    input_dict['sipDetails'][
                                                                        'sipPort'], 1500,
                                                                    sip_outbound_port,
                                                                    input_dict['chassisDetails'][
                                                                        'giVlan'],
                                                                    node_index['ims_index'])
            reserve_ports = reserve_ports + 1
            phy_eth_names_list.append(input_dict['sipDetails']['sipPort'].replace("v6", ""))
            if sip_node_param['Status'] is True:
                conf_obj = sip_node_param['conf_obj']
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure sip node parameters for the landslide test script"}
            if "QPP_IMS" in input_dict['scenario']:
                # rx_port=sip_outbound_port
                af_node_param = landslide_object.frame_node_parameters(conf_obj, "AfNodeIpAddr",
                                                                       input_dict['RxDetails'][
                                                                           'RxIp'],
                                                                       input_dict['RxDetails'][
                                                                           'RxGwIp'], 1,
                                                                       input_dict['RxDetails'][
                                                                           'RxPort'], 1500,
                                                                       sip_outbound_port,
                                                                       input_dict['chassisDetails'][
                                                                           'giVlanSupportZone'],
                                                                       node_index['ims_index'])
                reserve_ports = reserve_ports + 1
                phy_eth_names_list.append(input_dict['RxDetails']['RxPort'].replace("v6", ""))
                if af_node_param['Status'] is True:
                    conf_obj = af_node_param['conf_obj']
                    RobotLogger.log_logger.info("Ims Parameters framed successfully")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure af node parameters for the landslide test script"}
            else:
                af_outbound_port = input_dict['RxDetails']['RxPort'].replace("v6", "")
                # rx_port=af_outbound_port
                af_node_param = landslide_object.frame_node_parameters(conf_obj, "AfNodeIpAddr",
                                                                       input_dict['RxDetails'][
                                                                           'RxIp'],
                                                                       input_dict['RxDetails'][
                                                                           'RxGwIp'], 1,
                                                                       input_dict['RxDetails'][
                                                                           'RxPort'], 1500,
                                                                       af_outbound_port,
                                                                       input_dict['chassisDetails'][
                                                                           'giVlanSupportZone'],
                                                                       node_index['ims_index'])
                reserve_ports = reserve_ports + 1
                phy_eth_names_list.append(input_dict['RxDetails']['RxPort'].replace("v6", ""))
                if af_node_param['Status'] is True:
                    conf_obj = af_node_param['conf_obj']
                    RobotLogger.log_logger.info("Ims Parameters framed successfully")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure af node parameters for the landslide test script"}

            # Framing Dra node parameters
            if "QPP" in test_session_name:
                mog_port = input_dict['mogDetails']['mogPort'].replace("v6", "")
                dra_node_config = self.config_dra_node(conf_obj, input_dict, landslide_object,
                                                       node_index, tc_script_json,
                                                       phy_eth_names_list)
                if dra_node_config['Status'] is True:
                    conf_obj = dra_node_config['conf_obj']
                    phy_eth_names_list = dra_node_config['phy_eth_names_list']
                    RobotLogger.log_logger.info("DRA Node Configuration successful")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure DRA node parameters for the landslide test script"}

            # Enable port capture
            phy_eth_names_list = list(set(phy_eth_names_list))
            RobotLogger.log_logger.info(phy_eth_names_list)
            pc_param = landslide_object.frame_port_capture_parameters(conf_obj, len(phy_eth_names_list),
                                                                      phy_eth_names_list, ts_id,
                                                                      on_start=True)
            if pc_param['Status'] is True:
                conf_obj = pc_param['conf_obj']
                RobotLogger.log_logger.info("Framed port capture successfully")
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure port capture parameters for the landslide test script"}
            # Apply and Save the configuration
            conf_test_session = landslide_object.config_landslide_test_session(conf_obj,
                                                                               library_id,
                                                                               test_session_name)
            if conf_test_session['Status'] is True:
                # run_id = "1"
                # dmz_port = {}
                if "QPP" in test_session_name:
                    delay_step = 6
                else:
                    delay_step = 4
                return {'Status': 'True', 'Info': "Successfully Configured", 'trafficParameterList': "lib_id " + str(
                    library_id) + " tsname " + test_server_name + " delaystep " + str(
                    delay_step) + " logfilepath " + str(log_path) + " dmz_port " + str(dmz_port) + " mog_port " + str(
                    mog_port) + " gn_port " + str(gn_port) + " gi_port " + str(gi_port) + " rx_port " + str(rx_port)}
                # RobotLogger.log_logger.info("Return Dictionary Details:%s" % (return_dict))
                # print ("Return Value: %s" % (return_dict))
                # return return_dict
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure landslide test session parameters.Landslide REST POST operation failed."}
        except TypeError:
            RobotLogger.log_logger.debug(
                "TypeError occurred while configure the scenario:%s" % (str(traceback.format_exc())))
            return {'Status': 'False',
                    'Error': "TypeError occurred while configure the scenario"}
        except ValueError:
            RobotLogger.log_logger.debug(
                "OSError occurred while configure the scenario:%s " % (str(traceback.format_exc())))
            return {'Status': 'False',
                    'Error': "ValueError occurred while configure the scenario"}
        except IOError:
            RobotLogger.log_logger.debug(
                "IOError occurred while configure the scenario:%s " % (str(traceback.format_exc())))
            return {'Status': 'False',
                    'Error': "IOError occurred while configure the scenario"}
        except Exception:
            RobotLogger.log_logger.debug(
                "Exception occurred while configure the scenario :%s" % (str(traceback.format_exc())))
            return {'Status': 'False',
                    'Error': "Exception occurred while configure the scenario"}

    def basic_attach(self, input_parameter, landslide_object, traffic_list):
        """
            ######################################################################
                Title          :basic_attach()
                Description    : Configure Landslide configuration parameter for BASIC-ATTACH
                Parameters     :input_parameter - TCL input parameter list as string
                                landslide_object - Landslide object
                Return Value   : Configured test Session - Configured test session
                                 False - Exception while framing landslide config param
                Version  Author                  Date        Remarks
                0.1     Phanisree Y(py1780)      09/17/2018  Initial Draft
                0.2     Paulo Nicholas A(pa685w) 10/25/2018  [NIMB-6417]Enhanced
                        to support Enterprise Service
                0.3     Aman(as615p)             11/21/2018  [NIMB-6758]Enhanced
                        to support Packet Validation parameters
                0.4     Aman                   12/10/2018    [NIMB-6851] Added TCP support
                0.5     Phanisree Y(py1780)     01/24/2019   [NIMB-7295]Add SUT if not available in landslide TAS
            ######################################################################
        """

        try:
            # Dictionary for integer to boolean conversion
            int_bool_dict = {"0": "false", "1": "true"}
            # Dictionary for RAT to integer conversion
            rat_int_dict = {"4G": "6", "3G-S4": "1", "3G-GN": "1"}
            # Dictionary for PDN to integer conversion
            pdn_int_dict = {"ipv4": "1", "ipv6": "2", "ipv4v6": "3"}
            # convert list to dictionary --- method invoke from utilities.py
            util = UtilitiesLib()
            input_dict = util.list_to_dict_inputparam(input_parameter)
            # Required variables
            reserve_ports = 0
            phy_eth_names_list = []
            test_server_name = input_dict['chassisDetails']['testServer']
            library_name = input_dict['ue1Details']['msisdn1']
            test_session_name = input_dict['scenario']
            conf_obj = ""
            tc_name = ""
            tc_type = ""
            gn_port = input_dict['chassisDetails']['gnPort']
            dmz_port = "{}"
            gi_port = "{}"
            rx_port = "{}"
            mog_port = "{}"
            log_path = input_dict['logsPath']

            # Fetch library Id based on library name
            get_lib = landslide_object.get_library_details(library_name)
            if get_lib['Status'] is True:
                library_id = get_lib['Result']['id']
            else:
                return {'Status': 'False', 'Error': "Unable to retrieve library id for the landslide test script"}
            # Get Test server details
            get_ts_details = landslide_object.get_test_servers(test_server_name)
            if get_lib['Status'] is True:
                ts_id = get_ts_details["ts_id"]
            else:
                return {'Status': 'False', 'Error': "Unable to retrieve test server id for the landslide test script"}
            # Get test script
            json_obj = landslide_object.get_test_script_json(library_id, test_session_name)
            if json_obj['Status'] is True:
                tc_script_json = json_obj['json_res']
            else:
                return {'Status': 'False', 'Error': "Unable to get json object for the landslide test script"}

            # Set test instances for nodes Gn, AF, mog
            tc_inst = landslide_object.get_tc_inst(tc_script_json)
            if tc_inst['Status'] is True:
                node_index = tc_inst['tc_inst_dict']
                RobotLogger.log_logger.info("Node Index details: %s" % (node_index))
            else:
                RobotLogger.log_logger.debug("Unable to frame node index details")
                return {'Status': 'False',
                        'Error': "Unable to get node instance indexes  for the landslide test script"}

            # Frame Gn Node parameters
            gn_param_dict = {}
            pdp_type = input_dict['ue1Details']['ue1IpType'].lower()
            home_addr_type = pdn_int_dict[pdp_type]
            input_dict['HomeAddrType'] = home_addr_type
            # set radio access type from call type
            RobotLogger.log_logger.info("Rat Type Initial: %s" % (input_dict['callType']))
            rat_type = input_dict['callType'].upper()
            radio_access_type = rat_int_dict[rat_type]
            # set pci and pvi values
            RobotLogger.log_logger.info("PCI Initial: %s" % (input_dict['apn1Details']['apn1Pci']))
            RobotLogger.log_logger.info("PVI Initial: %s" % (input_dict['apn1Details']['apn1Pvi']))
            if "ENTERPRISE" in test_session_name:
                input_dict['apn1Details']['apn1Pci'] = str(input_dict['apn1Details'][
                                                               'apn1Pci']).lower()
                input_dict['apn1Details']['apn1Pvi'] = str(input_dict['apn1Details'][
                                                               'apn1Pvi']).lower()
            else:
                input_dict['apn1Details']['apn1Pci'] = int_bool_dict[input_dict['apn1Details'][
                    'apn1Pci']]
                input_dict['apn1Details']['apn1Pvi'] = int_bool_dict[input_dict['apn1Details'][
                    'apn1Pvi']]
            RobotLogger.log_logger.info("PCI After: %s" % (input_dict['apn1Details']['apn1Pci']))
            RobotLogger.log_logger.info("PVI After: %s" % (input_dict['apn1Details']['apn1Pvi']))

            if ("Roaming" in test_session_name and input_dict['callType'] != "3G-Gn"):
                gn_param_dict = {'Gtp2IncTaiEn': 'true',
                                 'Gtp2IncSaiEn': 'false',
                                 'Gtp2IncRaiEn': 'false',
                                 'Gtp2IncEcgiEn': 'true',
                                 'Gtp2N3Attempts': "5",
                                 'SessionRetries': 'false',
                                 'Gtp2ApnTotalApns_0': "1",
                                 'Gtp2ApnNumSpecifiedApns_0': "0",
                                 'Gtp2IncCgiEn': 'false', 'Gtp2T3Time': "3",
                                 'S5Protocol': 'GTPv2',
                                 'NtwkInterface': 'S5-S8',
                                 "HomeAddrType": home_addr_type,
                                 "Gtp2Imei": input_dict['ue1Details']['mei1'],
                                 "Gtp2Imsi": input_dict['ue1Details']['imsi1'],
                                 "Gtp2MsIsdn": input_dict[
                                     'ue1Details']['msisdn1'],
                                 "Gtp2RadioAccessType": rat_int_dict[
                                     input_dict['callType']],
                                 "Gtp2Mcc": input_dict['sgwDetails']['mcc1'],
                                 "Gtp2Mnc": input_dict['sgwDetails']['mnc1'],
                                 "Gtp2Tac": input_dict['sgwDetails']['tac1'],
                                 "Gtp2Ecgi": input_dict['sgwDetails'][
                                     'eCellId1'],
                                 "Gtp2AmbrDownlink": input_dict[
                                     'apn1Details']['apn1DownlinkAmbr'],
                                 "Gtp2AmbrUplink": input_dict[
                                     'apn1Details']['apn1UplinkAmbr'],
                                 "Gtp2Apn_0": input_dict[
                                     'apn1Details']['apn1Name'],
                                 "Gtp2QosClassId_1": input_dict[
                                     'apn1Details']['apn1Qci'],
                                 "Gtp2QosArpValue_1": input_dict[
                                     'apn1Details']['apn1Pl'],
                                 "Gtp2QosArpPreemptCapEn_1": input_dict['apn1Details']['apn1Pci'],
                                 "Gtp2QosArpPreemptVulnEn_1": input_dict['apn1Details']['apn1Pvi']}

            elif (input_dict['callType'] == "4G" or input_dict['callType'] == "3G-S4"):
                gn_param_dict = {'Gtp2Imsi': input_dict['ue1Details']['imsi1'],
                                 'Gtp2Imei': input_dict['ue1Details']['mei1'],
                                 'Gtp2MsIsdn': input_dict['ue1Details']['msisdn1'],
                                 'Gtp2RadioAccessType': radio_access_type,
                                 'Gtp2Mcc': input_dict['enodeB1Details']['mcc1'],
                                 'Gtp2Mnc': input_dict['enodeB1Details']['mnc1'],
                                 'Gtp2T3Time': '3', 'Gtp2N3Attempts': '5',
                                 'SessionRetries': 'false',
                                 'Gtp2CustomMsgEn': 'false',
                                 'HomeAddrType': home_addr_type,
                                 'Gtp2AmbrDownlink': input_dict['apn1Details']['apn1DownlinkAmbr'],
                                 'Gtp2AmbrUplink': input_dict['apn1Details']['apn1UplinkAmbr'],
                                 'Gtp2QosClassId_1': input_dict['apn1Details']['apn1Qci'],
                                 'Gtp2QosArpValue_1': input_dict['apn1Details']['apn1Pl'],
                                 'Gtp2QosArpPreemptCapEn_1': input_dict['apn1Details']['apn1Pci'],
                                 'Gtp2QosArpPreemptVulnEn_1': input_dict['apn1Details']['apn1Pvi'],
                                 'Gtp2Apn_0': input_dict['apn1Details']['apn1Name']}

                if input_dict['callType'] == "3G-S4":
                    temp_dict = {'Gtp2IncEcgiEn': 'false', 'Gtp2IncSaiEn': 'false',
                                 'Gtp2IncRaiEn': 'false',
                                 'Gtp2IncCgiEn': 'true',
                                 'Gtp2Lac': input_dict['rncDetails']['tac1'],
                                 'Gtp2Ci': input_dict['rncDetails']['eCellId1'],
                                 'TrafficMtu': 1400,
                                 'Gtp2IncTaiEn': 'false'}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
                elif input_dict['callType'] == "4G":
                    temp_dict = {'Gtp2IncTaiEn': 'true',
                                 'Gtp2IncEcgiEn': 'true',
                                 'Gtp2Tac': input_dict['enodeB1Details']['tac1'],
                                 'Gtp2Ecgi': input_dict['enodeB1Details']['eCellId1'],
                                 'TrafficMtu': input_dict['trafficDetails']['ueMtuSize'],
                                 'Gtp2IncSaiEn': 'false', 'Gtp2IncRaiEn': 'false',
                                 'Gtp2IncCgiEn': 'false'}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
                    traffic_list_upper = [element.upper() for element in traffic_list]
                    if any("TCP" in item for item in traffic_list_upper):
                        temp_dict = {'TrafficDontFragIp': 1}
                        gn_param_dict = {**gn_param_dict, **temp_dict}
                        del temp_dict
            elif input_dict['callType'] == "3G-Gn":
                max_bitrate_uplink = self.calculate_max_bit_rate(input_dict['apn1Details']
                                                                 ['apn1UplinkAmbr'])
                max_bitrate_downlink = self.calculate_max_bit_rate(input_dict['apn1Details']
                                                                   ['apn1DownlinkAmbr'])

                if (max_bitrate_uplink is False or max_bitrate_downlink is False):
                    RobotLogger.log_logger.info(
                        "Calculated uplink_mbr values are not in the range: %s" % max_bitrate_uplink)
                    RobotLogger.log_logger.info(
                        "Calculated downlink_mbr values are not in the range: %s" % max_bitrate_downlink)
                else:
                    if (int(max_bitrate_uplink) >= 8700) and (int(max_bitrate_uplink) <= 256000):
                        temp_dict = {'QosIncGbruMbruExt_0_0': 'true',
                                     'QosMaxBitrateUplinkExt_0_0': max_bitrate_uplink}
                        gn_param_dict = {**gn_param_dict, **temp_dict}
                        del temp_dict
                    if (int(max_bitrate_downlink) >= 8700) and (int(max_bitrate_downlink) <= 256000):
                        temp_dict = {'QosIncGbrdMbrdExt_0_0': 'true',
                                     'QosMaxBitrateDownlinkExt_0_0': max_bitrate_downlink}
                        gn_param_dict = {**gn_param_dict, **temp_dict}
                        del temp_dict
                gn_param_dict = {'NumMs': input_dict['ue1Details']['ueCount'],
                                 'Imsi': input_dict['ue1Details']['imsi1'],
                                 'MsIsdn': input_dict['ue1Details']['msisdn1'],
                                 'RatType': radio_access_type,
                                 'IncUli': 'true', 'UliMcc': input_dict['rncDetails']['mcc1'],
                                 'UliMnc': input_dict['rncDetails']['mnc1'],
                                 'UliCiSac': input_dict['rncDetails']['eCellId1'],
                                 'SmApn_0': input_dict['apn1Details']['apn1Name'],
                                 'PdpType': pdp_type,
                                 'IncRatType': 'true',
                                 'QosTrafficPriority_0_0': input_dict['apn1Details'][
                                     'apn1TrafficHandlingPriority'],
                                 'TrafficClass_0_0': input_dict['apn1Details']['apn1TrafficClass'],
                                 'QosIncSourceStatisticsDescriptor_0_0': 'true', 'T3Time': '3',
                                 'SessionRetries': 'false',
                                 'N3Attempts': '5', 'UliLac': input_dict['rncDetails']['tac1']}

            if input_dict['qppNegativeFlag'] == "True":
                gn_param_dict["Gtp2CustomMsgEn"] = "true"
            # Frame DMZ parameters for local host
            # traffic_enable = 1
            network_host = "Remote"
            # data_traffic = "Continuous"
            # dual_stack_en = "false"
            gn_param_dict['network_host'] = "Remote"

            # Framing Test Session Details for Landslide Test Session
            ts_param = landslide_object.frame_test_session_parameters(
                conf_obj, node_index['total_tc_inst'], library_id, test_server_name,
                test_session_name)
            if ts_param['Status'] is True:
                RobotLogger.log_logger.info("Conf_obj details: %s" % ts_param['conf_obj'])
                conf_obj = ts_param['conf_obj']
            else:
                return {'Status': 'False',
                        'Error': "Unable to frame test session parameters for the landslide test script"}

            # Configure the Gn landslide parameters
            ls_param = landslide_object.frame_landslide_parameters(conf_obj, gn_param_dict,
                                                                   tc_name,
                                                                   tc_type,
                                                                   node_index['gn_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
                RobotLogger.log_logger.info("ls_param details: %s" % ls_param['conf_obj'])
            else:
                RobotLogger.log_logger.debug("Unable to Frame Landslide Parameters")
                return {'Status': 'False', 'Error': "Unable to configure gn parameters for the landslide test script"}

            # Framing SGW sut details for Landslide Test Session
            if ((input_dict['roamingType'] == "nonroaming" and input_dict[
                'callType'] != "3G-Gn") or "QPP" in test_session_name):
                sgw1_ip = input_dict['gw1Details']['sgw1Ip']
                sgw1_ip = sgw1_ip.replace(".", "_")
                sgw_sut = landslide_object.add_sut(input_dict['gw1Details']['sgw1Ip'],
                                                   input_dict['gw1Details']['sgw1Ip'],
                                                   sgw1_ip)
                if sgw_sut['Status'] is True:
                    # conf_obj = sgw_sut_param['conf_obj']
                    RobotLogger.log_logger.info("Created SGW SUT Object: %s" % (conf_obj))
                else:
                    return {'Status': False,
                            'Error': "Unable to Create SGW sut parameters for the landslide test script"}
                sgw_param = landslide_object.frame_sut_parameters(conf_obj, "SgwSut", sgw1_ip,
                                                                  node_index['gn_index'])

                if sgw_param['Status'] is True:
                    conf_obj = sgw_param['conf_obj']
                    RobotLogger.log_logger.info("sgw_param details: %s" % sgw_param['conf_obj'])

                else:
                    RobotLogger.log_logger.debug("Unable to Frame SGW Parameters")
                    return {'Status': 'False',
                            'Error': "Unable to configure sgw sut parameters for the landslide test script"}

            # Framing SGW User sut details for Landslide Test Session
            if (((input_dict['roamingType'] == "domestic") or (input_dict['roamingType'] == "international")) and
                    input_dict['callType'] != "3G-Gn" and "QPP" not in test_session_name):
                # Framing Sgw control address for Landslide Test Session
                node_name = "SgwControlAddr"
                node_ip = input_dict['sgwDetails']['sgw1Ip']
                next_hop_ip = input_dict['sgwDetails']['sgw1GwIp']
                num_link_nodes = "1"
                phy_eth = input_dict['sgwDetails']['sgw1PhyName']
                mtu = 1500
                forced_eth = input_dict['sgwDetails']['sgw1PhyName']
                vlan_id = 0
                sgw_node_config = landslide_object.frame_node_parameters(conf_obj, node_name,
                                                                         node_ip,
                                                                         next_hop_ip,
                                                                         num_link_nodes,
                                                                         phy_eth, mtu,
                                                                         forced_eth,
                                                                         vlan_id, node_index[
                                                                             'gn_index'])
                if sgw_node_config['Status'] is True:
                    conf_obj = sgw_node_config['conf_obj']
                    reserve_ports = reserve_ports + 1
                    phy_eth_names_list.append(phy_eth)
                else:
                    return {'Status': 'False', 'Error': "SGW frame_node_parameters failed"}

            elif ((input_dict['roamingType'] == "nonroaming" and input_dict[
                'callType'] != "3G-Gn") or "QPP" in test_session_name):
                sgw1user_ip = input_dict['gw1Details']['sgw1S1uIp']
                sgw1user_ip = sgw1user_ip.replace(".", "_")
                sgw_user_sut = landslide_object.add_sut(input_dict['gw1Details']['sgw1S1uIp'],
                                                   input_dict['gw1Details']['sgw1S1uIp'],sgw1user_ip)
                if sgw_user_sut['Status'] is True:
                    # conf_obj = sgw_sut_param['conf_obj']
                    RobotLogger.log_logger.info("Created SGW user SUT Object: %s" % (conf_obj))
                else:
                    return {'Status': False,
                            'Error': "Unable to Create SGW user sut parameters for the landslide test script"}
                sgw_param = landslide_object.frame_sut_parameters(conf_obj,
                                                                  "SgwUserSut", sgw1user_ip,
                                                                  node_index['gn_index'])
                if sgw_param['Status'] is True:
                    conf_obj = sgw_param['conf_obj']
                    RobotLogger.log_logger.info("Config SGW User SUT Object: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure sgw user sut parameters for the landslide test script"}

            # Framing PGW sut details for Landslide Test Session
            if (((input_dict['roamingType'] == "domestic") or (input_dict['roamingType'] == "international")) and
                    input_dict['callType'] != "3G-Gn" and "QPP" not in test_session_name):
                pgw_node_name = "PgwSut"
            elif input_dict['callType'] == "3G-Gn":
                pgw_node_name = "SutGgsn"
            else:
                pgw_node_name = "PgwV4Sut"

            pgw1_ip = input_dict['gw1Details']['pgw1Ip']
            pgw1_ip = pgw1_ip.replace(".", "_")
            pgw_sut = landslide_object.add_sut(input_dict['gw1Details']['pgw1Ip'],
                                                    input_dict['gw1Details']['pgw1Ip'], pgw1_ip)
            if pgw_sut['Status'] is True:
                # conf_obj = sgw_sut_param['conf_obj']
                RobotLogger.log_logger.info("Created PGW SUT Object: %s" % (conf_obj))
            else:
                return {'Status': False,
                        'Error': "Unable to Create PGW sut parameters for the landslide test script"}
            pgw_param = landslide_object.frame_sut_parameters(conf_obj, pgw_node_name, pgw1_ip,
                                                              node_index['gn_index'])
            if pgw_param['Status'] is True:
                conf_obj = pgw_param['conf_obj']
                RobotLogger.log_logger.info("pgw_param details: %s" % pgw_param['conf_obj'])
            else:
                RobotLogger.log_logger.debug("Unable to Frame PGW Parameters")
                return {'Status': 'False',
                        'Error': "Unable to configure pgw sut parameters for the landslide test script"}

            if ((input_dict['callType'] == "4G" and input_dict[
                'roamingType'] == "nonroaming") or "QPP" in test_session_name):
                # Framing enodeB control address for Landslide Test Session
                enodeb_node_param = landslide_object.frame_node_parameters(conf_obj, "EnbUserAddr",
                                                                           input_dict[
                                                                               'enodeB1Details'][
                                                                               'enodeB1Ip'],
                                                                           input_dict[
                                                                               'enodeB1Details'][
                                                                               'enodeB1GwIp'],
                                                                           1,
                                                                           input_dict[
                                                                               'enodeB1Details'][
                                                                               'enodeB1PhyName'],
                                                                           1500, "",
                                                                           input_dict[
                                                                               'chassisDetails'][
                                                                               'gnVlan'],
                                                                           node_index['gn_index'])
                reserve_ports = reserve_ports + 1
                phy_eth_names_list.append(input_dict['enodeB1Details'][
                                              'enodeB1PhyName'].replace("v6", ""))
                if enodeb_node_param['Status'] is True:
                    conf_obj = enodeb_node_param['conf_obj']
                    RobotLogger.log_logger.info("enodeb_node_param details: %s" % enodeb_node_param['conf_obj'])
                else:
                    RobotLogger.log_logger.debug("Unable to Frame eNodeB Parameters")
                    return {'Status': 'False',
                            'Error': "Unable to configure enodeB node parameters for the landslide test script"}

                # Framing MMEcontrol address for Landslide Test Session
                mme_node_param = landslide_object.frame_node_parameters(conf_obj, "MmeControlAddr",
                                                                        input_dict['mme1Details'][
                                                                            'mme1Ip'],
                                                                        input_dict['mme1Details'][
                                                                            'mme1GwIp'], 1,
                                                                        input_dict['mme1Details'][
                                                                            'mme1PhyName'], 1500,
                                                                        input_dict['mme1Details'][
                                                                            'mme1PhyName'],
                                                                        input_dict[
                                                                            'chassisDetails'][
                                                                            'giVlan'],
                                                                        node_index['gn_index'])
                if mme_node_param['Status'] is True:
                    conf_obj = mme_node_param['conf_obj']
                    RobotLogger.log_logger.info("mme_node_param details: %s" % mme_node_param['conf_obj'])
                else:
                    RobotLogger.log_logger.debug("Unable to Frame MME Parameters")
                    return {'Status': 'False',
                            'Error': "Unable to configure mme node parameters for the landslide test script"}
            if ((input_dict['callType'] == "3G-S4" and input_dict['roamingType'] == "nonroaming") or input_dict[
                'callType'] == "3G-Gn"):
                # Framing RNC control address for Landslide Test Session
                rnc_node_param = landslide_object.frame_node_parameters(conf_obj, "SgsnUsrAddr",
                                                                        input_dict['rncDetails'][
                                                                            'rnc1Ip'],
                                                                        input_dict['rncDetails'][
                                                                            'rnc1GwIp'], 1,
                                                                        input_dict['rncDetails'][
                                                                            'rnc1PhyName'], 1500,
                                                                        input_dict['rncDetails'][
                                                                            'rnc1PhyName'],
                                                                        input_dict[
                                                                            'chassisDetails'][
                                                                            'gnVlan'],
                                                                        node_index['gn_index'])
                if rnc_node_param['Status'] is True:
                    conf_obj = rnc_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config rnc details: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure rnc node parameters for the landslide test script"}

                # Framing SGSN address for Landslide Test Session
                sgsn_node_param = landslide_object.frame_node_parameters(conf_obj, "SgsnCtlAddr",
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1Ip'],
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1GwIp'], 1,
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1PhyName'], 1500,
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1PhyName'],
                                                                         input_dict[
                                                                             'chassisDetails'][
                                                                             'gnVlan'],
                                                                         node_index['gn_index'])
                reserve_ports = reserve_ports + 1
                phy_eth_names_list.append(input_dict['sgsnDetails'][
                                              'sgsn1PhyName'].replace("v6", ""))
                if sgsn_node_param['Status'] is True:
                    conf_obj = sgsn_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config sgsn details: %s" % (conf_obj))
                    RobotLogger.log_logger.info("Gn Parameters framed successfully")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure sgsn node parameters for the landslide test script"}

            if input_dict['qppNegativeFlag'] is True:
                gn_param_dict["Gtp2CustomMsgEn"] = True
            # Frame DMZ parameters

            # Framing NetworkHostAddrLocal control address for Landslide Test Session
            # dmzOutboundPort = input_dict['sipDetails']['sipIp'].replace("v6", "")
            # dmzOutboundPort = ""
            # Framing DMZ Details
            dmz_config = self.configure_traffic(conf_obj, library_id, gn_param_dict, input_dict,
                                                landslide_object,
                                                node_index, traffic_list, phy_eth_names_list,
                                                home_addr_type,
                                                network_host)

            if dmz_config['Status'] is True:
                conf_obj = dmz_config['conf_obj']
                if "ENTERPRISE" not in test_session_name:
                    phy_eth_names_list = dmz_config['phy_eth_names_list']
                    dmz_port = input_dict['dmz1Details']['dmz1PhyName'].replace("v6", "")
                    RobotLogger.log_logger.info("DMZ Node and Traffic Configuration successful")
                else:
                    dmz_port = "0"
                    RobotLogger.log_logger.info("Traffic Configuration successful")
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure DMZ and Traffic Type node parameters for the landslide test script"}

            # Framing Dra node parameters
            if "QPP" in test_session_name:
                mog_port = input_dict['mogDetails']['mogPort'].replace("v6", "")
                dra_node_config = self.config_dra_node(conf_obj, input_dict, landslide_object,
                                                       node_index, tc_script_json,
                                                       phy_eth_names_list)
                if dra_node_config['Status'] is True:
                    conf_obj = dra_node_config['conf_obj']
                    phy_eth_names_list = dra_node_config['phy_eth_names_list']
                    RobotLogger.log_logger.info("DRA Node Configuration successful")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure DRA node parameters for the landslide test script"}

            # Enable port capture
            phy_eth_names_list = list(set(phy_eth_names_list))
            RobotLogger.log_logger.info(phy_eth_names_list)
            pc_param = landslide_object.frame_port_capture_parameters(conf_obj,
                                                                      len(phy_eth_names_list),
                                                                      phy_eth_names_list, ts_id,
                                                                      on_start=True)
            if pc_param['Status'] is True:
                conf_obj = pc_param['conf_obj']
                RobotLogger.log_logger.info("pc_param details: %s" % pc_param['conf_obj'])
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure port capture parameters for the landslide test script"}

            # Apply and Save the configuration
            conf_test_session = landslide_object.config_landslide_test_session(conf_obj,
                                                                               library_id,
                                                                               test_session_name)
            if conf_test_session['Status'] is True:
                # run_id = "1"
                # dmz_port = {}
                if "QPP" in test_session_name:
                    delay_step = 6
                elif "ENTERPRISE" in test_session_name:
                    delay_step = 2
                    dmz_port = "0"
                else:
                    delay_step = 4
                return {'Status': 'True', 'Info': "Successfully Configured", 'trafficParameterList': "lib_id " + str(
                    library_id) + " tsname " + test_server_name + " delaystep " + str(
                    delay_step) + " logfilepath " + str(log_path) + " dmz_port " + str(dmz_port) + " mog_port " + str(
                    mog_port) + " gn_port " + str(gn_port) + " gi_port " + str(gi_port) + " rx_port " + str(rx_port)}

                # RobotLogger.log_logger.info("Return Dictionary Details:%s" % (return_dict))
                # print ("Return Value: %s" % (return_dict))
                # return return_dict
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure landslide test session parameters.Landslide REST POST operation failed"}

        except TypeError:
            RobotLogger.log_logger.debug(
                "TypeError occurred while configure the scenario:%s" % (str(traceback.format_exc())))
            return {'Status': 'False',
                    'Error': "TypeError occurred while configure the scenario"}

        except ValueError:
            RobotLogger.log_logger.debug(
                "OSError occurred while configure the scenario:%s " % (str(traceback.format_exc())))
            return {'Status': 'False',
                    'Error': "ValueError occurred while configure the scenario"}
        except IOError:
            RobotLogger.log_logger.debug(
                "IOError occurred while configure the scenario:%s " % (str(traceback.format_exc())))
            return {'Status': 'False',
                    'Error': "IOError occurred while configure the scenario"}
        except Exception:
            RobotLogger.log_logger.debug(
                "Exception occurred while configure the scenario :%s" % (str(traceback.format_exc())))
            return {'Status': 'False',
                    'Error': "Exception occurred while configure the scenario"}

    def qpp_upliftment(self, input_parameter, landslide_object, feature, traffic_list):
        """
            ######################################################################
                Title          :qpp_upliftment()
                Description    : Configure Landslide configuration parameter for QPP-UPLIFTMENT
                Parameters     :input_parameter - TCL input parameter list as string
                                landslide_object - Landslide object
                                feature - feature like Data  or Ims for QPP
                Return Value   : Configured test Session - Configured test session
                                 False - Exception while framing landslide config param
                Version  Author                 Date        Remarks
                0.1     Phanisree Y(py1780) 09/17/2018  Initial Draft
            ######################################################################
        """
        try:
            if re.search("DATA", feature, re.IGNORECASE):
                result = self.basic_attach(input_parameter, landslide_object, traffic_list)
                RobotLogger.log_logger.info("QPP parameter configuration details: %s" % result)
                return result
            else:
                result = self.ir92_ir94_ipme(input_parameter, landslide_object)
                RobotLogger.log_logger.info("QPP parameter configuration details: %s" % result)
                return result
        except Exception:
            RobotLogger.log_logger.debug(
                "Exception occurred while configure qpp_upliftment:%s" % (str(traceback.format_exc())))
            return {'Status': 'False',
                    'Error': "Exception occurred while configure the scenario"}

    def data_ir92_ir94_ipme(self, input_parameter, landslide_object, traffic_list):
        """
            ######################################################################
                Title          :ir92_ir94_ipme()
                Description    : Configure Landslide configuration parameter for data_ir92_ir94_ipme
                Parameters     :input_parameter - TCL input parameter list as string
                                landslide_object - Landslide object
                Return Value   : Configured test Session - Configured test session
                                 False - Exception while framing landslide config param
                Version  Author                 Date        Remarks
                0.1     Debasish Nayak (dn8492) 10/17/2018  Initial Draft
                0.2     Phanisree Y(py1780)      01/24/2018 [NIMB-7295]Add SUT for pgw or sgw if not avaialble in TAS
            ######################################################################
        """

        try:
            # Dictionary for integer to boolean conversion
            int_bool_dict = {"0": "false", "1": "true"}
            # Dictionary for RAT to integer conversion
            rat_int_dict = {"4G": "6", "3GS4": "1", "3GGN": "1"}
            # Dictionary for PDN to integer conversion
            pdn_int_dict = {"ipv4": "1", "ipv6": "2", "ipv4v6": "3"}
            # convert list to dictionary --- method invoke from utilities.py
            RobotLogger.log_logger.info("Input parameter dictionary: %s" % (input_parameter))
            util = UtilitiesLib()
            input_dict = util.list_to_dict_inputparam(input_parameter)
            input_dict["Gtp2QosDetail"] = "PerBearer"
            RobotLogger.log_logger.info("Landslide Input parameter dictionary: %s" % (input_dict))
            # Required variables
            reserve_ports = 0
            phy_eth_names_list = []
            test_server_name = input_dict['chassisDetails']['testServer']
            RobotLogger.log_logger.info("Test server name: %s" % (test_server_name))
            library_name = input_dict['ue1Details']['msisdn1']
            test_session_name = input_dict['scenario']
            log_path = input_dict['logsPath']
            gn_port = input_dict['chassisDetails']['gnPort']
            dmz_port = "{}"
            gi_port = "{}"
            mog_port = "{}"
            rx_port = "{}"
            conf_obj = ""
            tc_name = ""
            tc_type = ""
            # Fetch library Id based on library name
            get_lib = landslide_object.get_library_details(library_name)
            if get_lib['Status'] is True:
                # library_id = get_lib["id"]
                library_id = get_lib['Result']['id']
                RobotLogger.log_logger.info("Library Id: %s" % (library_id))
            else:
                return {'Status': 'False', 'Error': "Unable to retrieve library id for the landslide test script"}
            # Get Test server details
            get_ts_details = landslide_object.get_test_servers(test_server_name)
            if get_lib['Status'] is True:
                ts_id = get_ts_details["ts_id"]
                RobotLogger.log_logger.info("Test server details: %s" % (ts_id))
            else:
                return {'Status': 'False', 'Error': "Unable to retrieve test server id for the landslide test script"}
            # Get test script
            json_obj = landslide_object.get_test_script_json(library_id, test_session_name)
            if json_obj['Status'] is True:
                tc_script_json = json_obj['json_res']
            else:
                return {'Status': 'False', 'Error': "Unable to get json object for the landslide test script"}
            # Set test instances for nodes Gn, AF, mog
            tc_inst = landslide_object.get_tc_inst(tc_script_json)
            if tc_inst['Status'] is True:
                node_index = tc_inst['tc_inst_dict']
                RobotLogger.log_logger.info("Node Index details: %s" % (node_index))
            else:
                RobotLogger.log_logger.debug("Unable to frame node index details")
                return {'Status': 'False',
                        'Error': "Unable to get node instance indexes  for the landslide test script"}

            # Frame Gn Node parameters
            gn_param_dict = {}
            pdp_type = input_dict['ue1Details']['ue1IpType'].lower()
            home_addr_type = pdn_int_dict[pdp_type]
            # set radio access type from call type
            rat_type = input_dict['callType'].upper()
            radio_access_type = rat_int_dict[rat_type]
            # set pci and pvi values
            RobotLogger.log_logger.info("PCI Initial: %s" % (input_dict['apn1Details']['apn1Pci']))
            RobotLogger.log_logger.info("PVI Initial: %s" % (input_dict['apn1Details']['apn1Pvi']))
            RobotLogger.log_logger.info("PCI Initial: %s" % (input_dict['apn2Details']['apn2Pci']))
            RobotLogger.log_logger.info("PVI Initial: %s" % (input_dict['apn2Details']['apn2Pvi']))
            input_dict['apn1Details']['apn1Pci'] = int_bool_dict[input_dict[
                'apn1Details']['apn1Pci']]
            input_dict['apn1Details']['apn1Pvi'] = int_bool_dict[input_dict[
                'apn1Details']['apn1Pvi']]
            input_dict['apn2Details']['apn2Pci'] = int_bool_dict[input_dict[
                'apn2Details']['apn2Pci']]
            input_dict['apn2Details']['apn2Pvi'] = int_bool_dict[input_dict[
                'apn2Details']['apn2Pvi']]

            RobotLogger.log_logger.info("PCI1 After: %s" % (input_dict['apn1Details']['apn1Pci']))
            RobotLogger.log_logger.info("PVI1 After: %s" % (input_dict['apn1Details']['apn1Pvi']))
            RobotLogger.log_logger.info("PCI2 After: %s" % (input_dict['apn2Details']['apn2Pci']))
            RobotLogger.log_logger.info("PVI2 After: %s" % (input_dict['apn2Details']['apn2Pvi']))

            input_dict['Gtp2CustomMsgEn'] = "false"
            gn_param_dict = {'Gtp2Imsi': input_dict['ue1Details']['imsi1'],
                             'Gtp2Imei': input_dict['ue1Details']['mei1'],
                             'Gtp2MsIsdn': input_dict['ue1Details']['msisdn1'],
                             'Gtp2RadioAccessType': radio_access_type,
                             'Gtp2Mcc': input_dict['enodeB1Details']['mcc1'],
                             'Gtp2Mnc': input_dict['enodeB1Details']['mnc1'],
                             'Gtp2T3Time': '3', 'Gtp2N3Attempts': '5',
                             'SessionRetries': 'false',
                             'Gtp2CustomMsgEn': input_dict['Gtp2CustomMsgEn'],
                             'HomeAddrType_1': home_addr_type,
                             'Gtp2AmbrDownlink': input_dict['apn1Details']['apn1DownlinkAmbr'],
                             'Gtp2AmbrUplink': input_dict['apn1Details']['apn1UplinkAmbr'],
                             'Gtp2QosDetail': input_dict["Gtp2QosDetail"],
                             'Gtp2QosClassId_1': input_dict['apn1Details']['apn1Qci'],
                             'Gtp2QosArpValue_1': input_dict['apn1Details']['apn1Pl'],
                             'Gtp2QosClassId_2': input_dict['apn1Details']['apn1Qci'],
                             'Gtp2QosArpValue_2': input_dict['apn1Details']['apn1Pl'],
                             'Gtp2QosClassId_3': input_dict['apn2Details']['apn2Qci'],
                             'Gtp2QosArpValue_3': input_dict['apn2Details']['apn2Pl'],
                             'Gtp2QosClassId_4': input_dict['apn2Details']['apn2Qci'],
                             'Gtp2QosArpValue_4': input_dict['apn2Details']['apn2Pl'],
                             'Gtp2QosArpPreemptCapEn_1': input_dict['apn1Details']['apn1Pci'],
                             'Gtp2QosArpPreemptVulnEn_1': input_dict['apn1Details']['apn1Pvi'],
                             'Gtp2QosArpPreemptCapEn_2': input_dict['apn1Details']['apn1Pci'],
                             'Gtp2QosArpPreemptVulnEn_2': input_dict['apn1Details']['apn1Pvi'],
                             'Gtp2QosArpPreemptCapEn_3': input_dict['apn2Details']['apn2Pci'],
                             'Gtp2QosArpPreemptVulnEn_3': input_dict['apn2Details']['apn2Pvi'],
                             'Gtp2QosArpPreemptCapEn_4': input_dict['apn2Details']['apn2Pci'],
                             'Gtp2QosArpPreemptVulnEn_4': input_dict['apn2Details']['apn2Pvi'],
                             'Gtp2Apn_0': input_dict['apn1Details']['apn1Name'],
                             'Gtp2IncTaiEn': 'true',
                             'Gtp2IncEcgiEn': 'true', 'Gtp2CfgFileEn': 'true',
                             'Gtp2Tac': input_dict['enodeB1Details']['tac1'],
                             'Gtp2Ecgi': input_dict['enodeB1Details']['eCellId1'],
                             'Gtp2IncSaiEn': 'false', 'Gtp2IncRaiEn': 'false',
                             'Gtp2IncCgiEn': 'false',
                             'VolteEn': 'true',
                             'DataTraffic': 'Continuous', 'Gtp2UliDbCmdCbRspEn': 'true',
                             'UeRtpAudioPort': 6000,
                             'UeRtpVideoPort': 7000, 'UeMsrpPort': 2855, 'UeRttPort': 8000,
                             'ImsNodeIpAddr': input_dict['sipDetails']['sipIp'],
                             'ImsNodePort': '5060',
                             'S5Protocol': 'GTPv2', 'ImsNodeType': 'Remote',
                             'ImsNodePcscfAddrType': '0',
                             'SipTransport': 'UDP', 'SipMaxMsgBufferSize': '2048'}
            if ("QPP_DATA_IR92" in input_dict['scenario']) or ("QPP_DATA_IR94" in input_dict['scenario']):
                network_host = "Local"
                gn_param_dict['network_host'] = "Local"
            else:
                network_host = "Remote"
                gn_param_dict['network_host'] = "Remote"

            if "MPMZ" in input_dict['scenario']:
                gn_param_dict['ApnToPgwMappingEn'] = "true"
                gn_param_dict['PgwApn_1'] = input_dict['apn1Details']['apn1Name']
                gn_param_dict['PgwApn_2'] = input_dict['apn2Details']['apn2Name']

            temp_dict = {'SipCallSetupEn': 'true', 'SipSubscriberUriScheme': '0',
                         'SipEndpointUriScheme': '0',
                         'UeCallStart': '1'}
            gn_param_dict = {**gn_param_dict, **temp_dict}
            del temp_dict
            if not "MT_Early_Media" in input_dict['scenario']:
                temp_dict = {'UeCallPending': 1000, 'UeCallLength': input_dict['audioDuration']}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict

            if "IPME_3G" in input_dict['scenario']:
                temp_dict = {'ServingNode': 'SGSN', 'UeCallLength': input_dict['audioDuration'],
                             'MsrpEn': 'true',
                             'UePattern': '2', 'RtpTrafficEn': 'false'}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
            if "IPME_N" in input_dict['scenario']:
                temp_dict = {'ServingNode': 'MME', 'UeCallLength': input_dict['audioDuration'],
                             'MsrpEn': 'true',
                             'UePattern': '2', 'RtpTrafficEn': 'false'}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict

            if ("IR92" in input_dict['scenario']) or ("QPP_DATA_IR92" in input_dict['scenario']):
                temp_dict = {'RtpTrafficEn': 'true', 'UeAuthenticationEn': 'true',
                             'RtpDmf1Type': 'Audio',
                             'RtpTrafficStartDelay': '1000', 'ServingNode': 'MME'}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
                temp_dict = {'UeCallLength': input_dict['audioDuration'], "UePattern": 2}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict

                if "IPME" in input_dict['scenario']:
                    temp_dict = {"DedicatedsPerDefaultBearer": 2, "MsrpEn": True}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
            elif ("IR94" in input_dict['scenario']) or ("QPP_DATA_IR94" in input_dict['scenario']):
                temp_dict = {"RtpTrafficEn": True, "UeAuthenticationEn": True,
                             "RtpDmf1Type": "Audio",
                             "RtpTrafficStartDelay": 1000, "UeVideoDelay": 0,
                             "UeReleaseMode": "Normal",
                             "RtpDmf2Type": "Video", "ServingNode": "MME", "UePattern": 2}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
                if "IPME" in input_dict['scenario']:
                    temp_dict = {"DedicatedsPerDefaultBearer": 3, "MsrpEn": True}
                    gn_param_dict = {**gn_param_dict, **temp_dict}
                    del temp_dict
            ts_param = landslide_object.frame_test_session_parameters(conf_obj,
                                                                      node_index['total_tc_inst'],
                                                                      library_id,
                                                                      test_server_name,
                                                                      test_session_name)
            if ts_param['Status'] is True:
                conf_obj = ts_param['conf_obj']
                RobotLogger.log_logger.info("Initial Config Object: %s" % (conf_obj))
            else:
                RobotLogger.log_logger.debug("Could not frame test server details")
                return {'Status': 'False',
                        'Error': "Unable to frame test session parameters for the landslide test script"}

            # Configure the Gn landslide parameters
            ls_param = landslide_object.frame_landslide_parameters(conf_obj, gn_param_dict,
                                                                   tc_name, tc_type,
                                                                   node_index['gn_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
                RobotLogger.log_logger.info("Gn Config Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure gn node parameters for the landslide test script"}

            # Framing SGW sut details for Landslide Test Session
            sgw1_ip = input_dict['gw1Details']['sgw1Ip']
            sgw1_ip = sgw1_ip.replace(".", "_")
            sgw_sut_param = landslide_object.add_sut(input_dict['gw1Details']['sgw1Ip'],
                                                     input_dict['gw1Details']['sgw1Ip'],
                                                     sgw1_ip)
            if sgw_sut_param['Status'] is True:
                # conf_obj = sgw_sut_param['conf_obj']
                RobotLogger.log_logger.info("Created SGW SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to Create sgw sut parameters for the landslide test script"}
            # Framing SGW sut details for Landslide Test Session
            sgw_param = landslide_object.frame_sut_parameters(conf_obj, "SgwSut", sgw1_ip,
                                                              node_index['gn_index'])
            if sgw_param['Status'] is True:
                conf_obj = sgw_param['conf_obj']
                RobotLogger.log_logger.info("Config SGW SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure sgw sut parameters for the landslide test script"}

            # Framing SGW User sut details for Landslide Test Session
            sgw1user_ip = input_dict['gw1Details']['sgw1S1uIp']
            sgw1user_ip = sgw1user_ip.replace(".", "_")
            sgw_user_sut_param = landslide_object.add_sut(input_dict['gw1Details']['sgw1S1uIp'],
                                                     input_dict['gw1Details']['sgw1S1uIp'],
                                                     sgw1user_ip)
            if sgw_user_sut_param['Status'] is True:
                # conf_obj = sgw_sut_param['conf_obj']
                RobotLogger.log_logger.info("Created SGW user SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to Create sgw user sut parameters for the landslide test script"}
            sgw_param = landslide_object.frame_sut_parameters(conf_obj, "SgwUserSut", sgw1user_ip,
                                                              node_index['gn_index'])
            if sgw_param['Status'] is True:
                conf_obj = sgw_param['conf_obj']
                RobotLogger.log_logger.info("Config SGW User SUT Object: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure sgw user sut parameters for the landslide test script"}

            # Framing PGW sut details for Landslide Test Session
            if "MPMZ" not in input_dict['scenario']:
                pgw1_ip = input_dict['gw1Details']['pgw1Ip']
                pgw1_ip = pgw1_ip.replace(".", "_")
                pgw_sut_param = landslide_object.add_sut(input_dict['gw1Details']['pgw1Ip'],
                                                         input_dict['gw1Details']['pgw1Ip'],
                                                         pgw1_ip)
                if pgw_sut_param['Status'] is True:
                    # conf_obj = sgw_sut_param['conf_obj']
                    RobotLogger.log_logger.info("Created PGW SUT Object: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to Create PGW sut parameters for the landslide test script"}
                pgw_param = landslide_object.frame_sut_parameters(conf_obj, "PgwV4Sut", pgw1_ip,
                                                                  node_index['gn_index'])
                if pgw_param['Status'] is True:
                    conf_obj = pgw_param['conf_obj']
                    RobotLogger.log_logger.info("Config PGW SUT Object: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure pgw sut parameters for the landslide test script"}
            elif "MPMZ" in input_dict['scenario']:
                pgw1_ip = input_dict['gw1Details']['pgw1Ip']
                pgw1_ip = pgw1_ip.replace(".", "_")
                pgw_sut_param = landslide_object.add_sut(input_dict['gw1Details']['pgw1Ip'],
                                                         input_dict['gw1Details']['pgw1Ip'],
                                                         pgw1_ip)
                if pgw_sut_param['Status'] is True:
                    # conf_obj = sgw_sut_param['conf_obj']
                    RobotLogger.log_logger.info("Created PGW SUT Object: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to Create PGW sut parameters for the landslide test script"}
                pgw_param = landslide_object.frame_sut_parameters(conf_obj, "PgwV4Sut_1",
                                                                  pgw1_ip,
                                                                  node_index['gn_index'])
                if pgw_param['Status'] is True:
                    conf_obj = pgw_param['conf_obj']
                    RobotLogger.log_logger.info("Config PGW SUT Object: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure pgw sut parameters for the landslide test script"}

                pgw2_ip = input_dict['gw2Details']['pgw2Ip']
                pgw2_ip = pgw2_ip.replace(".", "_")
                pgw_sut_param = landslide_object.add_sut(input_dict['gw2Details']['pgw2Ip'],
                                                         input_dict['gw2Details']['pgw2Ip'],
                                                         pgw2_ip)
                if pgw_sut_param['Status'] is True:
                    # conf_obj = sgw_sut_param['conf_obj']
                    RobotLogger.log_logger.info("Created PGW SUT Object: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to Create PGW sut parameters for the landslide test script"}
                pgw_param = landslide_object.frame_sut_parameters(conf_obj, "PgwV4Sut_2", pgw2_ip,
                                                                  node_index['gn_index'])
                if pgw_param['Status'] is True:
                    conf_obj = pgw_param['conf_obj']
                    RobotLogger.log_logger.info("Config PGW SUT Object: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure pgw sut parameters for the landslide test script"}
            if input_dict['callType'] == "4G":
                # Framing enodeB control address for Landslide Test Session
                enodeb_node_param = landslide_object.frame_node_parameters(conf_obj, "EnbUserAddr",
                                                                           input_dict[
                                                                               'enodeB1Details'][
                                                                               'enodeB1Ip'],
                                                                           input_dict[
                                                                               'enodeB1Details'][
                                                                               'enodeB1GwIp'],
                                                                           1,
                                                                           input_dict[
                                                                               'enodeB1Details'][
                                                                               'enodeB1PhyName'],
                                                                           1500, "",
                                                                           input_dict[
                                                                               'chassisDetails'][
                                                                               'gnVlan'],
                                                                           node_index['gn_index'])
                reserve_ports = reserve_ports + 1
                phy_eth_names_list.append(input_dict['enodeB1Details'][
                                              'enodeB1PhyName'].replace("v6", ""))
                RobotLogger.log_logger.info("Config enodeB details: %s" % (conf_obj))
                if enodeb_node_param['Status'] is True:
                    conf_obj = enodeb_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config enodeB details: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure enodeB node parameters for the landslide test script"}

                # Framing MMEcontrol address for Landslide Test Session
                mme_node_param = landslide_object.frame_node_parameters(conf_obj, "MmeControlAddr",
                                                                        input_dict['mme1Details'][
                                                                            'mme1Ip'],
                                                                        input_dict['mme1Details'][
                                                                            'mme1GwIp'], 1,
                                                                        input_dict['mme1Details'][
                                                                            'mme1PhyName'], 1500,
                                                                        input_dict['mme1Details'][
                                                                            'mme1PhyName'],
                                                                        input_dict[
                                                                            'chassisDetails'][
                                                                            'giVlan'],
                                                                        node_index['gn_index'])
                if mme_node_param['Status'] is True:
                    conf_obj = mme_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config mme details: %s" % (conf_obj))
                    RobotLogger.log_logger.info("Gn Parameters framed successfully")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure mme node parameters for the landslide test script"}
            elif input_dict['callType'] == "3G-S4":
                # Framing RNC control address for Landslide Test Session
                rnc_node_param = landslide_object.frame_node_parameters(conf_obj, "SgsnUsrAddr",
                                                                        input_dict['rncDetails'][
                                                                            'rnc1Ip'],
                                                                        input_dict['rncDetails'][
                                                                            'rnc1GwIp'], 1,
                                                                        input_dict['rncDetails'][
                                                                            'rnc1PhyName'], 1500,
                                                                        input_dict['rncDetails'][
                                                                            'rnc1PhyName'],
                                                                        input_dict[
                                                                            'chassisDetails'][
                                                                            'gnVlan'],
                                                                        node_index['gn_index'])
                if rnc_node_param['Status'] is True:
                    conf_obj = rnc_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config rnc details: %s" % (conf_obj))
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure rnc node parameters for the landslide test script"}

                # Framing SGSN address for Landslide Test Session
                sgsn_node_param = landslide_object.frame_node_parameters(conf_obj, "SgsnCtlAddr",
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1Ip'],
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1GwIp'], 1,
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1PhyName'], 1500,
                                                                         input_dict['sgsnDetails'][
                                                                             'sgsn1PhyName'],
                                                                         input_dict[
                                                                             'chassisDetails'][
                                                                             'gnVlan'],
                                                                         node_index['gn_index'])
                reserve_ports = reserve_ports + 1
                if sgsn_node_param['Status'] is True:
                    conf_obj = sgsn_node_param['conf_obj']
                    RobotLogger.log_logger.info("Config sgsn details: %s" % (conf_obj))
                    RobotLogger.log_logger.info("Gn Parameters framed successfully")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure sgsn node parameters for the landslide test script"}

            # Framing DMZ Details
            dmz_config = self.configure_traffic(conf_obj, library_id, gn_param_dict, input_dict,
                                                landslide_object,
                                                node_index, traffic_list,
                                                phy_eth_names_list,
                                                home_addr_type,
                                                network_host)

            if dmz_config['Status'] is True:
                conf_obj = dmz_config['conf_obj']
                phy_eth_names_list = dmz_config['phy_eth_names_list']
                RobotLogger.log_logger.info("DMZ Node and Traffic Configuration successful")
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure DMZ and Traffic Type node parameters for the landslide test script"}

            # Framing Gtp2ApnSpecified_0 for Dual APN
            apn_list = [input_dict['apn1Details']['apn1Name'], input_dict['apn2Details']['apn2Name']]
            dualapn_config = landslide_object.frame_multiple_network_hosts_parameters(
                conf_obj, "Gtp2ApnSpecified_0", apn_list, node_index['gn_index'])
            if dualapn_config['Status'] is True:
                conf_obj = dualapn_config['conf_obj']
                RobotLogger.log_logger.info("DualAPN_config Details: %s" % dualapn_config['conf_obj'])
            else:
                RobotLogger.log_logger.debug("Unable to Frame DualAPN_config Parameters")
                return {'Status': 'False',
                        'Error': "Unable to configure DualAPN_config parameters for the landslide test script"}
            # Create TDF (.csv) file in log path
            data_header = "IMSI,MS ISDN Number,Access Point Name,Aggregate Max Bit Rate Downlink,Aggregate Max Bit Rate Uplink"

            imsi1 = input_dict['ue1Details']['imsi1']
            msisdn1 = input_dict['ue1Details']['msisdn1']
            apn1_name = input_dict['apn1Details']['apn1Name']
            apn1_downlink_ambr = input_dict['apn1Details']['apn1DownlinkAmbr']
            apn1_uplink_ambr = input_dict['apn1Details']['apn1UplinkAmbr']
            apn2_name = input_dict['apn2Details']['apn2Name']
            apn2_downlink_ambr = input_dict['apn2Details']['apn2DownlinkAmbr']
            apn2_uplink_ambr = input_dict['apn2Details']['apn2UplinkAmbr']
            data = data_header + "\n" + imsi1 + "," + msisdn1 + "," + apn1_name + "," + apn1_downlink_ambr + "," + apn1_uplink_ambr + "\n" + imsi1 + "," + msisdn1 + "," + apn2_name + "," + apn2_downlink_ambr + "," + apn2_uplink_ambr
            file_name = input_dict['logsPath'] + "/" + input_dict['tdfFileName']
            RobotLogger.log_logger.debug("TDF File Name:%s" % (file_name))
            RobotLogger.log_logger.debug("TDF File Data:%s" % (data))
            try:
                file_handle = open(file_name, "w+")
                file_handle.write(data)
                file_handle.close()
            except IOError:
                RobotLogger.log_logger.debug("IOError occurred while creating tdf file.")

            except Exception as error:
                print('Error: TDF File: File does not exists: {}'.format(error))

            # Add tdf file
            add_tdf = landslide_object.add_tdf(library_id, input_dict['logsPath'],
                                               input_dict['tdfFileName'])

            if add_tdf['Status'] is True:
                # conf_obj = add_tdf['conf_obj']
                RobotLogger.log_logger.info("add_tdf file Details: %s" % add_tdf)
            else:
                RobotLogger.log_logger.debug("Unable to add_tdf files Parameters")
                return {'Status': 'False',
                        'Error': "Unable to add_tdf files parameters for the landslide test script"}

            # Framing TDF Details
            frame_tdf_param = landslide_object.frame_tdf_parameters(conf_obj, "Gtp2CfgFile",
                                                                    library_id,
                                                                    input_dict['tdfFileName'],
                                                                    node_index['gn_index'])

            if frame_tdf_param['Status'] is True:
                conf_obj = frame_tdf_param['conf_obj']
                RobotLogger.log_logger.info("frame_tdf_param details: %s" % (ls_param))
            else:
                RobotLogger.log_logger.debug("Unable to Frame frame_tdf_param Parameters")
                return {'Status': 'False',
                        'Error': "Unable to frame_tdf_param for the landslide test script"}

            # Framing IMS node parameters

            sip_outbound_port = input_dict['sipDetails']['sipPort'].replace("v6", "")
            dmz_port = sip_outbound_port
            af_outbound_port = input_dict['RxDetails']['RxPort'].replace("v6", "")
            rx_port = af_outbound_port

            ims_node_config = self.config_ims_node(conf_obj, input_dict, landslide_object,
                                                   node_index,
                                                   tc_script_json,
                                                   phy_eth_names_list)
            if ims_node_config['Status'] is True:
                conf_obj = ims_node_config['conf_obj']
                phy_eth_names_list = ims_node_config['phy_eth_names_list']
                RobotLogger.log_logger.info("IMS Node Configuration successful")
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure IMS node parameters for the landslide test script"}

            # Framing Dra node parameters

            if "QPP" in test_session_name:
                mog_port = input_dict['mogDetails']['mogPort'].replace("v6", "")
                dra_node_config = self.config_dra_node(conf_obj, input_dict, landslide_object,
                                                       node_index, tc_script_json,
                                                       phy_eth_names_list)
                if dra_node_config['Status'] is True:
                    conf_obj = dra_node_config['conf_obj']
                    phy_eth_names_list = dra_node_config['phy_eth_names_list']
                    RobotLogger.log_logger.info("DRA Node Configuration successful")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure DRA node parameters for the landslide test script"}

            # Enable port capture
            phy_eth_names_list = list(set(phy_eth_names_list))
            RobotLogger.log_logger.info(phy_eth_names_list)
            pc_param = landslide_object.frame_port_capture_parameters(conf_obj,
                                                                      len(phy_eth_names_list),
                                                                      phy_eth_names_list, ts_id,
                                                                      on_start=True)
            if pc_param['Status'] is True:
                conf_obj = pc_param['conf_obj']
                RobotLogger.log_logger.info("Framed port capture successfully")
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure port capture parameters for the landslide test script"}
            # Apply and Save the configuration
            conf_test_session = landslide_object.config_landslide_test_session(conf_obj, library_id,
                                                                               test_session_name)
            if conf_test_session['Status'] is True:
                # run_id = "1"
                delay_step = 6
                return {'Status': 'True', 'Info': "Successfully Configured", 'trafficParameterList': "lib_id " + str(
                    library_id) + " tsname " + test_server_name + " delaystep " + str(
                    delay_step) + " logfilepath " + str(log_path) + " dmz_port " + str(dmz_port) + " mog_port " + str(
                    mog_port) + " gn_port " + str(gn_port) + " gi_port " + str(gi_port) + " rx_port " + str(rx_port)}

            else:
                return {'Status': 'False',
                        'Error': "Unable to configure landslide test session parameters.Landslide REST POST operation failed."}
        except TypeError:
            RobotLogger.log_logger.debug(
                "TypeError occurred while configure the scenario data_ir92_ir94_ipme:%s" % (
                    str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "TypeError occurred while configure data_ir92_ir94_ipme"}
        except ValueError:
            RobotLogger.log_logger.debug(
                "ValueError occurred while configure the scenario data_ir92_ir94_ipme:%s " % (
                    str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "ValueError occurred while configure data_ir92_ir94_ipme"}
        except IOError:
            RobotLogger.log_logger.debug(
                "IOError occurred while configure the scenario data_ir92_ir94_ipme:%s " % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "IOError occurred while configure data_ir92_ir94_ipme"}
        except Exception:
            RobotLogger.log_logger.debug(
                "Exception occurred while configure the scenario data_ir92_ir94_ipme:%s" % (
                    str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "Exception occurred while configure data_ir92_ir94_ipme"}

    def x2_ho(self, input_parameter, landslide_object):
        """
        ######################################################################
            Title          : x2_ho()
            Description    : Configure Landslide configuration parameter for
                             X2_HO
            Parameters     : input_parameter - TCL input parameter list as
                             string
                            landslide_object - Landslide object
            Return Value   : Configured test Session - Configured test session
                             False - Exception while framing landslide config
                                     param
            Version  Author                  Date        Remarks
            0.1     Paulo Nicholas A(pa685w) 10/10/2018  Initial Draft
            0.2     Paulo Nicholas A(pa685w) 10/15/2018  Added duration and
                                            useGratuitousArp parameters
            0.3     Priyank(pg685w)         11/21/2018  [NIMB-6766] added
                                                        condition to remove v6
                                                        while appending the
                                                        port to port capture list
            Version  Author                  Date        Remarks
            0.1     Vinod kumar(vr760k)     10/12/2018  Given review comment to
                    add duration and useGratuitousArp parameters
        ######################################################################
        """

        try:
            # Dictionary for integer to boolean conversion
            int_bool_dict = {"0": "false", "1": "true"}
            # Dictionary for PDN to integer conversion
            pdn_int_dict = {"ipv4": "1", "ipv6": "2", "ipv4v6": "3"}
            # convert list to dictionary --- method invoke from utilities.py
            util = UtilitiesLib()
            input_dict = util.list_to_dict_inputparam(input_parameter)
            # home_address = pdn_int_dict[input_dict['pdnType'].lower()]
            # Required variables
            reserve_ports = 0
            phy_eth_names_list = []
            test_server_name = input_dict['chassis1Details']['testServer']
            library_name = input_dict['ue1Details']['msisdn1']
            test_session_name = input_dict['scenario']
            log_path = input_dict['logsPath']
            conf_obj = ""
            tc_name = ""
            tc_type = ""
            # Fetch library Id based on library name
            get_lib = landslide_object.get_library_details(library_name)
            if get_lib['Status'] is True:
                libraries = get_lib['Result']
                library_id = libraries['id']
            else:
                return {'Status': False, 'Error': "Failed to fetch library id"}
            # Get Test server details
            get_ts_details = landslide_object.get_test_servers(test_server_name)
            if get_lib['Status'] is True:
                test_server_id = get_ts_details["ts_id"]
            else:
                return {'status': False, 'info': 'Failed to get test server details'}
            # Get test script
            json_obj = landslide_object.get_test_script_json(library_id,
                                                             test_session_name)
            if json_obj['Status'] is True:
                tc_script_json = json_obj['json_res']
            else:
                return {'status': False, 'info': 'Failed to get test session session details'}
            # Get test instances for nodes Gn,Gi
            tc_inst = landslide_object.get_tc_inst(tc_script_json)
            if tc_inst['Status'] is True:
                node_index = tc_inst['tc_inst_dict']
            else:
                return {'status': False, 'info': 'Failed to get test session instance details'}
            # Frame Gn Node parameters
            gn_param_dict = {}
            home_addr_type = pdn_int_dict[input_dict['ue1Details'][
                'ue1IpType'].lower()]
            # Frame test session parameter
            ts_param = landslide_object.frame_test_session_parameters(
                conf_obj, node_index['total_tc_inst'], library_id,
                test_server_name, test_session_name)
            if ts_param['Status'] is True:
                conf_obj = ts_param['conf_obj']
            else:
                return {'Status': False, 'Error': "Failed to frame basic landslide test session parameters"}
            # Configuring All Gn LTE stack parameters
            gn_param_dict = {'Gtp2Imsi': input_dict['ue1Details']['imsi1'],
                             'Gtp2Imei': input_dict['ue1Details']['mei1'],
                             'Gtp2MsIsdn': input_dict['ue1Details']['msisdn1'],
                             'Gtp2RadioAccessType': 6,
                             'Gtp2Mcc': input_dict['enodeB1Details']['mcc1'],
                             'Gtp2Mnc': input_dict['enodeB1Details']['mnc1'],
                             'Gtp2T3Time': '3', 'Gtp2N3Attempts': '5',
                             'SessionRetries': 'false',
                             'Gtp2CustomMsgEn': 'false',
                             'HomeAddrType': home_addr_type,
                             'Gtp2AmbrDownlink': input_dict['apn1Details'][
                                 'apn1DownlinkAmbr'],
                             'Gtp2AmbrUplink': input_dict['apn1Details'][
                                 'apn1UplinkAmbr'],
                             'Gtp2QosClassId_1': input_dict['apn1Details'][
                                 'apn1Qci'],
                             'Gtp2QosArpValue_1': input_dict['apn1Details'][
                                 'apn1Pl'],
                             'Gtp2QosArpPreemptCapEn_1': int_bool_dict[
                                 input_dict['apn1Details']['apn1Pci']],
                             'Gtp2QosArpPreemptVulnEn_1': int_bool_dict[
                                 input_dict['apn1Details']['apn1Pvi']],
                             'Gtp2Apn_0': input_dict['apn1Details'][
                                 'apn1Name'], 'Gtp2IncTaiEn': 'true',
                             'Gtp2IncEcgiEn': 'true', 'Gtp2Tac': input_dict[
                    'enodeB1Details']['tac1'],
                             'Gtp2Ecgi': input_dict['enodeB1Details'][
                                 'eCellId1'],
                             'Gtp2IncSaiEn': 'false', 'Gtp2IncRaiEn': 'false',
                             'Gtp2IncCgiEn': 'false'}
            # Configure X2-H0 Gn Specific parameters
            gn_param_dict["TgtGtp2IncModUli"] = "true"
            gn_param_dict["TgtGtp2IncTaiEn"] = "true"
            gn_param_dict["TgtGtp2IncEcgiEn"] = "true"
            gn_param_dict["TgtGtp2Mcc"] = input_dict['enodeB2Details']['mcc2']
            gn_param_dict["TgtGtp2Mnc"] = input_dict['enodeB2Details']['mnc2']
            gn_param_dict["TgtGtp2Tac"] = input_dict['enodeB2Details']['tac2']
            gn_param_dict["TgtGtp2Ecgi"] = input_dict['enodeB2Details'][
                'eCellId2']
            gn_param_dict["MobilityMode"] = "Single Handoff"
            gn_param_dict["MobilityTimeMs"] = str(int(input_dict[
                                                          'mobilityTimeline1Details']['mobilityInterval']) * 1000)
            gn_param_dict["NetworkHostNatedTrafficEn"] = "true"
            gn_param_dict["TgtGtp2IncModApnAmbr"] = "true"
            # Set duration as "0"
            gn_param_dict["duration"] = 0
            # Set Gratuitous Arp as True
            gn_param_dict["useGratuitousArp"] = str(True)
            # Configure SGW Relocation
            if input_dict['sgwRelocation'] == "true":
                # Enable SGW reloc flag
                gn_param_dict["SgwRelocationEn"] = "true"
            # Frame DMZ parameters for local host
            # traffic_enable = 1
            gn_param_dict['NetworkHost'] = "Local"
            gn_param_dict['DataTraffic'] = "Continuous"
            # Enable dual stack configuration as required on Dmz node
            if home_addr_type == "3":
                gn_param_dict['DualStackEn'] = "true"
            else:
                gn_param_dict['DualStackEn'] = "false"
            # Configure the Gn landslide parameters
            ls_param = landslide_object.frame_landslide_parameters(
                conf_obj, gn_param_dict, tc_name, tc_type,
                node_index['gn_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
            else:
                return {'Status': False, 'Error': "frame_landslide_parameters failed"}
            # Create PgwSut dictionary and assign in gn_param_dict
            pgw1_ip = input_dict['gw1Details']['pgw1Ip']
            pgw1_sut_name = pgw1_ip.replace(".", "_")
            # Add SUT to the Landslide inventory
            pgw1_add_sut = landslide_object.add_sut(pgw1_ip, '1.2.3.4', pgw1_sut_name)
            if pgw1_add_sut['Status'] is False:
                return {'Status': False, 'Error': "Failed to add PGW SUT to the LS inventory"}
            # Framing PGW sut details for Landslide Test Session
            pgw1_param = landslide_object.frame_sut_parameters(
                conf_obj, "PgwV4Sut", pgw1_sut_name, node_index['gn_index'])
            if pgw1_param['Status'] is True:
                conf_obj = pgw1_param['conf_obj']
            else:
                return {'Status': False, 'Error': "frame_sut_parameters failed"}
            # Create SGW SUT dictionary
            sgw1_ip = input_dict['gw1Details']['sgw1Ip']
            sgw1_sut_name = sgw1_ip.replace(".", "_")
            sgw1_add_sut = landslide_object.add_sut(sgw1_ip,
                                                    management_ip='1.2.3.4',
                                                    sut_name=sgw1_sut_name)
            if sgw1_add_sut['Status'] is False:
                return {'Status': False, 'Error': "Failed to add SGW SUT to the LS inventory"}
            # Framing PGW sut details for Landslide Test Session
            sgw1_param = landslide_object.frame_sut_parameters(
                conf_obj, "SgwSut", sgw1_sut_name, node_index['gn_index'])
            if sgw1_param['Status'] is True:
                conf_obj = sgw1_param['conf_obj']
            else:
                return {'Status': False, 'Error': "frame_sut_parameters failed"}
            # Create SGW-User SUT dictionary
            sgw1_s1u_ip = input_dict['gw1Details']['sgw1S1uIp']
            sgw1_s1u_sut_name = sgw1_s1u_ip.replace(".", "_")
            # RobotLogger.log_logger.info("Landslide Gn Parameters: %s" % (gn_param_dict))
            # Add SUT to the Landslide inventory
            sgw1_s1u_add_sut = landslide_object.add_sut(
                ip_address=sgw1_s1u_ip, management_ip='1.2.3.4',
                sut_name=sgw1_s1u_sut_name)
            if sgw1_s1u_add_sut['Status'] is False:
                return {'Status': False, 'Error': "Failed to add SGW1-User  SUT to the LS inventory"}
            # Framing PGW sut details for Landslide Test Session
            sgw1_s1u_param = landslide_object.frame_sut_parameters(
                conf_obj, "SgwUserSut", sgw1_s1u_sut_name,
                node_index['gn_index'])
            if sgw1_s1u_param['Status'] is True:
                conf_obj = sgw1_s1u_param['conf_obj']
            else:
                return {'Status': False, 'Error': "frame_sut_parameters failed"}
            # Add relocated SGW detail
            if input_dict['sgwRelocation'] == "true":
                # Create SGW SUT dictionary
                sgw2_ip = input_dict['gw2Details']['sgw2Ip']
                sgw2_sut_name = sgw2_ip.replace(".", "_")
                # Add SUT to the Landslide inventory
                sgw2_add_sut = landslide_object.add_sut(
                    sgw2_ip, management_ip='1.2.3.4', sut_name=sgw2_sut_name)
                if sgw2_add_sut['Status'] is False:
                    return {'Status': False, 'Error': "Failed to add SGW2 SUT to the LS inventory"}
                sgw2_param = landslide_object.frame_sut_parameters(
                    conf_obj, "MobSgwSut", sgw2_sut_name,
                    node_index['gn_index'])
                if sgw2_param['Status'] is True:
                    conf_obj = sgw2_param['conf_obj']
                else:
                    return {'Status': False, 'Error': "frame_sut_parameters failed"}
                # Create SGW-User SUT dictionary
                sgw2_s1u_ip = input_dict['gw2Details']['sgw2S1uIp']
                sgw2_s1u_sut_name = sgw2_s1u_ip.replace(".", "_")
                # Add SUT to the Landslide inventory
                sgw2_s1u_add_sut = landslide_object.add_sut(
                    sgw2_s1u_ip, management_ip='1.2.3.4',
                    sut_name=sgw2_s1u_sut_name)
                if sgw2_s1u_add_sut['Status'] is False:
                    return {'Status': False, 'Error': "Failed to add SGW1-User  SUT to the LS inventory"}
                # Framing PGW sut details for Landslide Test Session
                sgw2_s1u_param = landslide_object.frame_sut_parameters(
                    conf_obj, "MobSgwUserSut", sgw2_s1u_sut_name,
                    node_index['gn_index'])
                if sgw2_s1u_param['Status'] is True:
                    conf_obj = sgw2_s1u_param['conf_obj']
                else:
                    return {'Status': False, 'Error': "frame_sut_parameters failed"}
            # Framing enodeB control address for Landslide Test Session
            enode_b_1_node_param = landslide_object.frame_node_parameters(
                conf_obj, "EnbUserAddr", input_dict['enodeB1Details'][
                    'enodeB1Ip'], input_dict['enodeB1Details']['enodeB1GwIp'],
                1, input_dict['enodeB1Details']['enodeB1PhyName'], 1500,
                "", input_dict['chassis1Details']['gnVlan'],
                node_index['gn_index'])
            reserve_ports = reserve_ports + 1
            phy_eth = input_dict['enodeB1Details'][
                'enodeB1PhyName'].replace("v6", "")
            phy_eth_names_list.append(phy_eth)
            RobotLogger.log_logger.info("Config enodeB details: %s" % (conf_obj))
            if enode_b_1_node_param['Status'] is True:
                conf_obj = enode_b_1_node_param['conf_obj']
                RobotLogger.log_logger.info("Config enodeB1 details: %s" % (conf_obj))
            else:
                return {'Status': False,
                        'Error': "Unable to configure enodeB1 node parameters for the landslide test script"}
            # Framing MMEcontrol address for Landslide Test Session
            mme_node1_param = landslide_object.frame_node_parameters(
                conf_obj, "MmeControlAddr", input_dict['mme1Details'][
                    'mme1Ip'], input_dict['mme1Details']['mme1GwIp'], 1,
                input_dict['mme1Details']['mme1PhyName'], 1500,
                input_dict['mme1Details']['mme1PhyName'],
                input_dict['chassis1Details']['giVlan'],
                node_index['gn_index'])
            if mme_node1_param['Status'] is True:
                conf_obj = mme_node1_param['conf_obj']
                RobotLogger.log_logger.info("Config mme details: %s" % (conf_obj))
                RobotLogger.log_logger.info("Gn Parameters framed successfully")
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure mme node parameters for the landslide test script"}
            # Framing enodeB control address for Landslide Test Session
            enode_b_2_node_param = landslide_object.frame_node_parameters(
                conf_obj, "MobEnbUserAddr", input_dict['enodeB2Details'][
                    'enodeB2Ip'], input_dict['enodeB2Details']['enodeB2GwIp'],
                1, input_dict['enodeB2Details']['enodeB2PhyName'], 1500, "",
                input_dict['chassis1Details']['gnVlan'],
                node_index['gn_index'])
            reserve_ports = reserve_ports + 1
            phy_eth_names_list.append(input_dict['enodeB2Details'][
                                          'enodeB2PhyName'].replace("v6", ""))
            RobotLogger.log_logger.info("Config enodeB2 details: %s" % (conf_obj))
            if enode_b_2_node_param['Status'] is True:
                conf_obj = enode_b_2_node_param['conf_obj']
                RobotLogger.log_logger.info("Config enodeB2 details: %s" % (conf_obj))
            else:
                return {'Status': False,
                        'Error': "Unable to configure enodeB2 node parameters for the landslide test script"}
            # Framing Dmz node parameters
            if home_addr_type == "3":
                dmz_v4_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "Ipv4NetworkHostAddrLocal",
                    input_dict['dmz1Details']['dmz1Ip'],
                    input_dict['dmz1Details']['dmz1GwIp'], "1",
                    input_dict['dmz1Details']['dmz1PhyName'], 1500,
                    "", input_dict['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_v4_node_param['Status'] is True:
                    conf_obj = dmz_v4_node_param['conf_obj']
                else:
                    return {'Status': False, 'Error': "DMZv6 frame_node_parameters failed"}
                dmz_v6_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "Ipv6NetworkHostAddrLocal",
                    input_dict['dmz1Details']['dmz1Ipv6'],
                    input_dict['dmz1Details']['dmz1GwIpv6'], "1",
                    input_dict['dmz1Details']['dmz1PhyNamev6'], 1500,
                    "", input_dict['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_v6_node_param['Status'] is True:
                    conf_obj = dmz_v6_node_param['conf_obj']
                else:
                    return {'Status': False, 'Error': "DMZv6 frame_node_parameters failed"}
            else:
                dmz_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "NetworkHostAddrLocal",
                    input_dict['dmz1Details']['dmz1Ip'],
                    input_dict['dmz1Details']['dmz1GwIp'], "1",
                    input_dict['dmz1Details']['dmz1PhyName'], 1500,
                    "", input_dict['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_node_param['Status'] is True:
                    conf_obj = dmz_node_param['conf_obj']
                else:
                    return {'Status': False, 'Error': "DMZ frame_node_parameters failed"}
            phy_eth = list(set(phy_eth_names_list))
            reserve_ports = reserve_ports + 1
            dmz_port = input_dict['dmz1Details']['dmz1PhyName'].replace("v6", "")
            phy_eth_names_list.append(dmz_port)
            phy_eth_names_list = list(set(phy_eth_names_list))
            total_ports = len(phy_eth_names_list)
            RobotLogger.log_logger.info(
                "Port Capture List: {}, Total ports count: {}".format(phy_eth_names_list, total_ports))
            # Enable port capture
            pc_param = landslide_object.frame_port_capture_parameters(
                conf_obj, total_ports, phy_eth_names_list, test_server_id,
                on_start=True)
            if pc_param['Status'] is True:
                conf_obj = pc_param['conf_obj']
            else:
                RobotLogger.log_logger.info("Failed to frame ports")
                return {'Status': False, 'Error': "frame_port_capture_parameters failed"}
            # Apply and Save the configuration
            conf_test_session = landslide_object.config_landslide_test_session(
                conf_obj, library_id, test_session_name)
            if conf_test_session['Status'] is True:
                delay_step = "2"
                return {'Status': True, 'Info': "Successfully Configured", 'trafficParameterList': "lib_id " + str(
                    library_id) + " tsname " + test_server_name + " delaystep " + delay_step + " logfilepath " + str(
                    log_path) + " dmz_port " + str(dmz_port) + " gn_port " + str(phy_eth[0])}
            else:
                return {'Status': False, 'Error': "Configuration failed"}
        except TypeError:
            RobotLogger.log_logger.debug("TypeError occurred while configure X2_HO:%s" % (str(traceback.format_exc())))
            return {'Status': False, 'Error': "TypeError occurred while configure X2_HO"}
        except ValueError:
            RobotLogger.log_logger.debug(
                "ValueError occurred while configure X2_HO:%s " % (str(traceback.format_exc())))
            return {'Status': False, 'Error': "ValueError occurred while configure X2_HO"}
        except IOError:
            RobotLogger.log_logger.debug("IOError occurred while configure X2_HO:%s " % (str(traceback.format_exc())))
            return {'Status': False, 'Error': "IOError occurred while configure X2_HO"}
        except Exception:
            RobotLogger.log_logger.debug("Exception occurred while configure X2_HO:%s" % (str(traceback.format_exc())))
            return {'Status': False, 'Error': "Exception occurred while configure X2_HO"}

    def s1_ho(self, input_parameter, landslide_object):
        """
            ######################################################################
                Title          :s1_ho()
                Description    : Configure Landslide configuration parameter for S1-HO
                Parameters     :input_parameter - TCL input parameter list as string
                                landslide_object - Landslide object
                Return Value   : Configured test Session - Configured test session
                                 False - Exception while framing landslide config param
                Version  Author                 Date        Remarks
                0.1     Vinod Rajupeta (vr760k) 10/08/2018  Initial Draft

                Review Version  Author                 Date        Remarks
                0.1    Abuzar                       10/15/2018  To implement the headers
                0.2    Priyank(pg685w)              11/21/2018 [NIMB-6766] added condition
                                                               to remove v6 while appending
                                                               the port to port capture list
            ######################################################################
        """

        try:
            # Dictionary for integer to boolean conversion
            int_bool_dict = {"0": "false", "1": "true"}
            # Dictionary for PDN to integer conversion
            pdn_int_dict = {"ipv4": "1", "ipv6": "2", "ipv4v6": "3"}
            # convert list to dictionary
            util = UtilitiesLib()
            input_dict = util.list_to_dict_inputparam(input_parameter)
            home_address = pdn_int_dict[input_dict['pdnType'].lower()]
            # Required variables
            reserve_ports = 0
            phy_eth_names_list = []
            test_server_name = input_dict['chassis1Details']['testServer']
            library_name = input_dict['ue1Details']['msisdn1']
            test_session_name = input_dict['scenario']
            log_path = input_dict['logsPath']
            conf_obj = ""
            tc_name = ""
            tc_type = ""

            # Fetch library Id based on library name
            get_lib = landslide_object.get_library_details(library_name)
            if get_lib['Status'] is True:
                libraries = get_lib['Result']
                library_id = libraries['id']
            else:
                return {'Status': 'False', 'Error': "Failed to fetch library id"}

            # Get Test server details
            get_ts_details = landslide_object.get_test_servers(test_server_name)
            if get_lib['Status'] is True:
                test_server_id = get_ts_details["ts_id"]
            else:
                return {'status': False, 'info': 'Failed to get test server details'}

            # Get test script
            json_obj = landslide_object.get_test_script_json(library_id, test_session_name)
            if json_obj['Status'] is True:
                tc_script_json = json_obj['json_res']
            else:
                return {'status': False, 'info': 'Failed to get test session session details'}

            # Get test instances for nodes Gn,Gi
            tc_inst = landslide_object.get_tc_inst(tc_script_json)
            if tc_inst['Status'] is True:
                node_index = tc_inst['tc_inst_dict']
            else:
                return {'status': False, 'info': 'Failed to get test session instance details'}

            # Frame Gn Node parameters
            gn_param_dict = {}
            home_addr_type = pdn_int_dict[input_dict['ue1Details']['ue1IpType'].lower()]

            # convert pci and pvi values 0 or 1 to True or False
            input_dict['apn1Details']['apn1Pci'] = int_bool_dict[input_dict[
                'apn1Details']['apn1Pci']]
            input_dict['apn1Details']['apn1Pvi'] = int_bool_dict[input_dict[
                'apn1Details']['apn1Pvi']]

            # Configure eNodeB details
            ts_param = landslide_object.frame_test_session_parameters(
                conf_obj, node_index['total_tc_inst'], library_id, test_server_name,
                test_session_name)
            if ts_param['Status'] is True:
                conf_obj = ts_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "Failed to frame basic landslide test session parameters"}

            # Configuring All Gn LTE stack parameters
            gn_param_dict = {'Gtp2Imsi': input_dict['ue1Details']['imsi1'],
                             'Gtp2Imei': input_dict['ue1Details']['mei1'],
                             'Gtp2MsIsdn': input_dict['ue1Details']['msisdn1'],
                             'Gtp2RadioAccessType': 6,
                             'Gtp2Mcc': input_dict['enodeB1Details']['mcc1'],
                             'Gtp2Mnc': input_dict['enodeB1Details']['mnc1'],
                             'Gtp2T3Time': '3', 'Gtp2N3Attempts': '5', 'Gtp2CustomMsgEn': 'false',
                             'SessionRetries': 'false',
                             'HomeAddrType': home_addr_type,
                             'Gtp2AmbrDownlink': input_dict['apn1Details']['apn1DownlinkAmbr'],
                             'Gtp2AmbrUplink': input_dict['apn1Details']['apn1UplinkAmbr'],
                             'Gtp2QosClassId_1': input_dict['apn1Details']['apn1Qci'],
                             'Gtp2QosArpValue_1': input_dict['apn1Details']['apn1Pl'],
                             'Gtp2QosArpPreemptCapEn_1': input_dict['apn1Details']['apn1Pci'],
                             'Gtp2QosArpPreemptVulnEn_1': input_dict['apn1Details']['apn1Pvi'],
                             'Gtp2Apn_0': input_dict['apn1Details']['apn1Name'],
                             'Gtp2IncTaiEn': 'true',
                             'Gtp2IncEcgiEn': 'true', 'Gtp2Tac': input_dict[
                    'enodeB1Details']['tac1'],
                             'Gtp2Ecgi': input_dict['enodeB1Details']['eCellId1'],
                             'Gtp2IncSaiEn': 'false', 'Gtp2IncRaiEn': 'false',
                             'Gtp2IncCgiEn': 'false'}

            # Configure S1-H0 Gn Specific parameters
            gn_param_dict["TgtGtp2IncModUli"] = "true"
            gn_param_dict["TgtGtp2IncTaiEn"] = "true"
            gn_param_dict["TgtGtp2IncEcgiEn"] = "true"

            gn_param_dict["TgtGtp2Mcc"] = input_dict['enodeB2Details']['mcc2']
            gn_param_dict["TgtGtp2Mnc"] = input_dict['enodeB2Details']['mnc2']
            gn_param_dict["TgtGtp2Tac"] = input_dict['enodeB2Details']['tac2']
            gn_param_dict["TgtGtp2Ecgi"] = input_dict['enodeB2Details']['eCellId2']
            gn_param_dict["MobilityMode"] = "Single Handoff"
            gn_param_dict["MobilityTimeMs"] = str(
                int(input_dict['mobilityTimeline1Details']['mobilityInterval']) * 1000)
            gn_param_dict["NetworkHostNatedTrafficEn"] = "true"
            gn_param_dict["TgtGtp2IncModApnAmbr"] = "true"

            # Configure SGW Reloccation
            if input_dict['sgwRelocation'] == "true":
                # Enable SGW reloc flag
                gn_param_dict["SgwRelocationEn"] = "true"
                # Configure SGW Mobility SUT - MobSgwSut & MobSgwUserSut

            if input_dict['mmeChange'] == "true":
                gn_param_dict['MobMmeControlAddrErrInj'] = "0"
            # Frame DMZ parameters for local host
            # traffic_enable = 1
            gn_param_dict['NetworkHost'] = "Local"
            gn_param_dict['DataTraffic'] = "Continuous"

            # Enable dual stack configuration as required on Dmz node
            if home_addr_type == "3":
                gn_param_dict['DualStackEn'] = "true"
            else:
                gn_param_dict['DualStackEn'] = "false"
            # Configure the Gn landslide parameters
            ls_param = landslide_object.frame_landslide_parameters(
                conf_obj, gn_param_dict, tc_name, tc_type,
                node_index['gn_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_landslide_parameters failed"}
            # Configure basic LS parameters
            conf_obj['duration'] = 0
            conf_obj['useGratuitousArp'] = str(True)
            # Create PgwSut dictionary and assign in gn_param_dict
            pgw1_ip = input_dict['gw1Details']['pgw1Ip']
            pgw1_sut_name = pgw1_ip.replace(".", "_")

            # Add SUT to the Landslide inventory
            # pgw1_add_sut = landslide_object.add_sut(ip_address=pgw1_ip,
            # management_ip='1.2.3.4', sut_name=pgw1_sut_name)
            pgw1_add_sut = landslide_object.add_sut(pgw1_ip, '1.2.3.4', pgw1_sut_name)
            if pgw1_add_sut['Status'] is False:
                return {'Status': 'False', 'Error': "Failed to add PGW SUT to the LS inventory"}

            # Framing PGW sut details for Landslide Test Session
            pgw1_param = landslide_object.frame_sut_parameters(conf_obj, "PgwV4Sut", pgw1_sut_name,
                                                               node_index['gn_index'])
            if pgw1_param['Status'] is True:
                conf_obj = pgw1_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_sut_parameters failed"}

            # Create SGW SUT dictionary and assign in gn_param_dict
            sgw1_ip = input_dict['gw1Details']['sgw1Ip']
            sgw1_sut_name = sgw1_ip.replace(".", "_")

            # Add SUT to the Landslide inventory
            sgw1_add_sut = landslide_object.add_sut(ip_address=sgw1_ip,
                                                    management_ip='1.2.3.4',
                                                    sut_name=sgw1_sut_name)
            if sgw1_add_sut['Status'] is False:
                return {'Status': 'False', 'Error': "Failed to add SGW SUT to the LS inventory"}

            # Framing PGW sut details for Landslide Test Session
            sgw1_param = landslide_object.frame_sut_parameters(
                conf_obj, "SgwSut", sgw1_sut_name, node_index['gn_index'])
            if sgw1_param['Status'] is True:
                conf_obj = sgw1_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_sut_parameters failed"}

            # Create SGW-User SUT dictionary and assign to gn_param_dict
            sgw1_s1u_ip = input_dict['gw1Details']['sgw1S1uIp']
            sgw1_s1u_sut_name = sgw1_s1u_ip.replace(".", "_")

            # Add SUT to the Landslide inventory
            sgw1_s1u_add_sut = landslide_object.add_sut(ip_address=sgw1_s1u_ip,
                                                        management_ip='1.2.3.4',
                                                        sut_name=sgw1_s1u_sut_name)
            if sgw1_s1u_add_sut['Status'] is False:
                return {'Status': 'False', 'Error': "Failed to add SGW1-User  SUT to the LS inventory"}

            # Framing PGW sut details for Landslide Test Session
            sgw1_s1u_param = landslide_object.frame_sut_parameters(conf_obj, "SgwUserSut",
                                                                   sgw1_s1u_sut_name,
                                                                   node_index['gn_index'])
            if sgw1_s1u_param['Status'] is True:
                conf_obj = sgw1_s1u_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_sut_parameters failed"}
            # Add relocated SGW detail
            if input_dict['sgwRelocation'] == "true":
                # Create SGW SUT dictionary
                sgw2_ip = input_dict['gw2Details']['sgw2Ip']
                sgw2_sut_name = sgw2_ip.replace(".", "_")
                # Add SUT to the Landslide inventory
                sgw2_add_sut = landslide_object.add_sut(ip_address=sgw2_ip,
                                                        management_ip='1.2.3.4',
                                                        sut_name=sgw2_sut_name)
                if sgw2_add_sut['Status'] is False:
                    return {'Status': 'False', 'Error': "Failed to add SGW2 SUT to the LS inventory"}
                sgw2_param = landslide_object.frame_sut_parameters(conf_obj, "MobSgwSut",
                                                                   sgw2_sut_name,
                                                                   node_index['gn_index'])
                if sgw2_param['Status'] is True:
                    conf_obj = sgw2_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "frame_sut_parameters failed"}
                # Create SGW-User SUT dictionary
                sgw2_s1u_ip = input_dict['gw2Details']['sgw2S1uIp']
                sgw2_s1u_sut_name = sgw2_s1u_ip.replace(".", "_")

                # Add SUT to the Landslide inventory
                sgw2_s1u_add_sut = landslide_object.add_sut(ip_address=sgw2_s1u_ip,
                                                            management_ip='1.2.3.4',
                                                            sut_name=sgw2_s1u_sut_name)
                if sgw2_s1u_add_sut['Status'] is False:
                    return {'Status': 'False', 'Error': "Failed to add SGW1-User  SUT to the LS inventory"}

                # Framing PGW sut details for Landslide Test Session
                sgw2_s1u_param = landslide_object.frame_sut_parameters(conf_obj, "MobSgwUserSut",
                                                                       sgw2_s1u_sut_name,
                                                                       node_index['gn_index'])
                if sgw2_s1u_param['Status'] is True:
                    conf_obj = sgw2_s1u_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "frame_sut_parameters failed"}
            # Node parameters configuration
            # Framing enodeB control address for Landslide Test Session
            enodeb1_node_param = landslide_object.frame_node_parameters(conf_obj, "EnbUserAddr",
                                                                        input_dict[
                                                                            'enodeB1Details'][
                                                                            'enodeB1Ip'],
                                                                        input_dict[
                                                                            'enodeB1Details'][
                                                                            'enodeB1GwIp'], 1,
                                                                        input_dict[
                                                                            'enodeB1Details'][
                                                                            'enodeB1PhyName'],
                                                                        1500, "",
                                                                        input_dict[
                                                                            'chassis1Details'][
                                                                            'gnVlan'],
                                                                        node_index['gn_index'])
            reserve_ports = reserve_ports + 1
            phy_eth = input_dict['enodeB1Details']['enodeB1PhyName'].replace("v6", "")
            phy_eth_names_list.append(phy_eth)
            RobotLogger.log_logger.info("Config enodeB details: %s" % (conf_obj))
            if enodeb1_node_param['Status'] is True:
                conf_obj = enodeb1_node_param['conf_obj']
                RobotLogger.log_logger.info("Config enodeB1 details: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure enodeB1 node parameters for the landslide test script"}

            # Framing MMEcontrol address for Landslide Test Session
            mme_node1_param = landslide_object.frame_node_parameters(conf_obj, "MmeControlAddr",
                                                                     input_dict['mme1Details'][
                                                                         'mme1Ip'],
                                                                     input_dict['mme1Details'][
                                                                         'mme1GwIp'], 1,
                                                                     input_dict['mme1Details'][
                                                                         'mme1PhyName'], 1500,
                                                                     input_dict['mme1Details'][
                                                                         'mme1PhyName'],
                                                                     input_dict['chassis1Details'][
                                                                         'giVlan'],
                                                                     node_index['gn_index'])
            if mme_node1_param['Status'] is True:
                conf_obj = mme_node1_param['conf_obj']
                RobotLogger.log_logger.info("Config mme details: %s" % (conf_obj))
                RobotLogger.log_logger.info("Gn Parameters framed successfully")
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure mme node parameters for the landslide test script"}

            # Add inter MME relocation
            if input_dict['mmeChange'] == "true":
                mme_node2_param = landslide_object.frame_node_parameters(conf_obj,
                                                                         "MobMmeControlAddr",
                                                                         input_dict['mme2Details'][
                                                                             'mme2Ip'],
                                                                         input_dict['mme2Details'][
                                                                             'mme2GwIp'], 1,
                                                                         input_dict['mme2Details'][
                                                                             'mme2PhyName'], 1500,
                                                                         input_dict['mme2Details'][
                                                                             'mme2PhyName'],
                                                                         input_dict[
                                                                             'chassis1Details'][
                                                                             'giVlan'],
                                                                         node_index['gn_index'])
                if mme_node2_param['Status'] is True:
                    conf_obj = mme_node2_param['conf_obj']
                    RobotLogger.log_logger.info("Config mme details: %s" % (conf_obj))
                    RobotLogger.log_logger.info("Inter MME configured successfully")
                else:
                    return {'Status': 'False',
                            'Error': "Unable to configure mme node parameters for the landslide test script"}

            # Framing enodeB control address for Landslide Test Session
            enodeb2_node_param = landslide_object.frame_node_parameters(conf_obj, "MobEnbUserAddr",
                                                                        input_dict[
                                                                            'enodeB2Details'][
                                                                            'enodeB2Ip'],
                                                                        input_dict[
                                                                            'enodeB2Details'][
                                                                            'enodeB2GwIp'],
                                                                        1,
                                                                        input_dict[
                                                                            'enodeB2Details'][
                                                                            'enodeB2PhyName'],
                                                                        1500, "",
                                                                        input_dict[
                                                                            'chassis1Details'][
                                                                            'gnVlan'],
                                                                        node_index['gn_index'])
            reserve_ports = reserve_ports + 1
            phy_eth_names_list.append(input_dict['enodeB2Details'][
                                          'enodeB2PhyName'].replace("v6", ""))
            RobotLogger.log_logger.info("Config enodeB2 details: %s" % (conf_obj))
            if enodeb2_node_param['Status'] is True:
                conf_obj = enodeb2_node_param['conf_obj']
                RobotLogger.log_logger.info("Config enodeB2 details: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure enodeB2 node parameters for the landslide test script"}
            # Framing Dmz node parameters
            if home_addr_type == "3":
                dmz_v4_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "Ipv4NetworkHostAddrLocal",
                    input_dict['dmz1Details']['dmz1Ip'],
                    input_dict['dmz1Details']['dmz1GwIp'], "1",
                    input_dict['dmz1Details']['dmz1PhyName'], 1500,
                    "", input_dict['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_v4_node_param['Status'] is True:
                    conf_obj = dmz_v4_node_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "DMZv6 frame_node_parameters failed"}
                dmz_v6_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "Ipv6NetworkHostAddrLocal",
                    input_dict['dmz1Details']['dmz1Ipv6'],
                    input_dict['dmz1Details']['dmz1GwIpv6'], "1",
                    input_dict['dmz1Details']['dmz1PhyNamev6'], 1500,
                    "", input_dict['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_v6_node_param['Status'] is True:
                    conf_obj = dmz_v6_node_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "DMZv6 frame_node_parameters failed"}
            else:
                dmz_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "NetworkHostAddrLocal",
                    input_dict['dmz1Details']['dmz1Ip'],
                    input_dict['dmz1Details']['dmz1GwIp'], "1",
                    input_dict['dmz1Details']['dmz1PhyName'], 1500,
                    "", input_dict['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_node_param['Status'] is True:
                    conf_obj = dmz_node_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "DMZ frame_node_parameters failed"}
            phy_eth = list(set(phy_eth_names_list))
            reserve_ports = reserve_ports + 1
            dmz_port = input_dict['dmz1Details']['dmz1PhyName'].replace("v6", "")
            phy_eth_names_list.append(dmz_port)
            phy_eth_names_list = list(set(phy_eth_names_list))
            toatl_ports = len(phy_eth_names_list)
            RobotLogger.log_logger.info(
                "Port Capture List: {}, Total ports count : {}".format(phy_eth_names_list, toatl_ports))
            # Enable port capture
            pc_param = landslide_object.frame_port_capture_parameters(
                conf_obj, toatl_ports, phy_eth_names_list, test_server_id,
                on_start=True)
            if pc_param['Status'] is True:
                conf_obj = pc_param['conf_obj']
            else:
                RobotLogger.log_logger.info("Failed to frame ports")
                return {'Status': 'False', 'Error': "frame_port_capture_parameters failed"}
            # Apply and Save the configuration
            conf_test_session = landslide_object.config_landslide_test_session(
                conf_obj, library_id, test_session_name)
            if conf_test_session['Status'] is True:
                delay_step = "2"
                # phy_list_str = ' '.join(phy_eth_names_list)
                return {'Status': 'True', 'Info': "Successfully Configured", 'trafficParameterList': "lib_id " + str(
                    library_id) + " tsname " + test_server_name + " delaystep " + delay_step + " logfilepath " + str(
                    log_path) + " dmz_port " + str(dmz_port) + " gn_port " + str(phy_eth[0]) + " home_address " + str(
                    home_address)}
            else:
                return {'Status': 'False', 'Error': "Configuration failed"}
        except TypeError:
            RobotLogger.log_logger.debug("TypeError occurred while configure S1-HO:%s" % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "TypeError occurred while configure S1-HO"}
        except ValueError:
            RobotLogger.log_logger.debug(
                "ValueError occurred while configure S1-HO:%s " % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "ValueError occurred while configure S1-HO"}
        except IOError:
            RobotLogger.log_logger.debug("IOError occurred while configure S1-HO:%s " % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "IOError occurred while configure S1-HO"}
        except Exception:
            RobotLogger.log_logger.debug("Exception occurred while configure S1-HO:%s" % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "Exception occurred while configure S1-HO"}

    def inter_rat(self, input_parameter, landslide_object):
        """
            ######################################################################
                Title          :inter_rat()
                Description    : Configure Landslide parameters for all inter_rat scenarios
                Parameters     :input_parameter - TCL input parameter list as string
                                landslide_object - Landslide object
                Return Value   : Configured test Session - Configured test session
                                 False - Exception while framing landslide config param
                Version  Author                 Date        Remarks
                0.1     Ananya G(ag699f)       10/10/2018  Initial Draft
                0.2     Ananya G(ag699f)       10/17/2018  Added support for conversion
                										   from dualStack to single
                0.3     Priyank(pg685w)         11/21/2018 [NIMB-6766] added condition
                                                            to remove v6 while appending
                                                            the port to port capture list
            ######################################################################
        """

        try:
            # Dictionary for integer to boolean conversion
            int_bool_dict = {"0": "false", "1": "true"}
            # Dictionary for RAT to integer conversion
            # rat_int_dict = {"4G": "6", "3GS4": "1", "3GGn": "1"}
            # Dictionary for PDN to integer conversion
            pdn_int_dict = {"ipv4": "1", "ipv6": "2", "ipv4v6": "3"}
            # convert list to dictionary --- method invoke from utilities.py
            util = UtilitiesLib()
            input_dict = util.list_to_dict_inputparam(input_parameter)
            home_address = pdn_int_dict[input_dict['pdnType'].lower()]
            # Required variables
            reserve_ports = 0
            phy_eth_names_list = []
            test_server_name = input_dict['chassis1Details']['testServer']
            library_name = input_dict['ue1Details']['msisdn1']
            test_session_name = input_dict['scenario']
            log_path = input_dict['logsPath']
            conf_obj = ""
            tc_name = ""
            tc_type = ""

            # Fetch library Id based on library name
            get_lib = landslide_object.get_library_details(library_name)
            if get_lib['Status'] is True:
                libraries = get_lib['Result']
                library_id = libraries['id']
            else:
                return {'Status': 'False', 'Error': "Failed to fetch library id"}

            # Get Test server details
            get_ts_details = landslide_object.get_test_servers(test_server_name)
            if get_lib['Status'] is True:
                test_server_id = get_ts_details["ts_id"]
            else:
                return {'status': False, 'info': 'Failed to get test server details'}

            # Get test script
            json_obj = landslide_object.get_test_script_json(library_id, test_session_name)
            if json_obj['Status'] is True:
                tc_script_json = json_obj['json_res']
            else:
                return {'status': False, 'info': 'Failed to get test session session details'}

            # Get test instances for nodes Gn,Gi
            tc_inst = landslide_object.get_tc_inst(tc_script_json)
            if tc_inst['Status'] is True:
                node_index = tc_inst['tc_inst_dict']
            else:
                return {'status': False, 'info': 'Failed to get test session instance details'}
            # Frame Gn Node parameters
            gn_param_dict = {}
            home_addr_type = pdn_int_dict[input_dict['ue1Details']['ue1IpType'].lower()]
            # radio_access_type = rat_int_dict[input_dict['callType'].upper()] #
            # -------------->Not required
            # convert pci and pvi values 0 or 1 to True or False
            input_dict['apn1Details']['apn1Pci'] = int_bool_dict[input_dict['apn1Details'][
                'apn1Pci']]
            input_dict['apn1Details']['apn1Pvi'] = int_bool_dict[input_dict['apn1Details'][
                'apn1Pvi']]

            # Configure eNodeB details
            ts_param = landslide_object.frame_test_session_parameters(conf_obj, node_index
            ['total_tc_inst'],
                                                                      library_id,
                                                                      test_server_name,
                                                                      test_session_name)
            if ts_param['Status'] is True:
                conf_obj = ts_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "Failed to frame basic landslide test session parameters"}

            # Configuring All Gn LTE stack parameters
            gn_param_dict = {'TestActivity': 'Inter Technology Mobility',
                             'Gtp2Imsi': input_dict['ue1Details']['imsi1'],
                             'Gtp2Imei': input_dict['ue1Details']['mei1'],
                             'Gtp2MsIsdn': input_dict['ue1Details']['msisdn1'],
                             'Gtp2RadioAccessType': 6,
                             'Gtp2Mcc': input_dict['enodeB1Details']['mcc1'],
                             'Gtp2Mnc': input_dict['enodeB1Details']['mnc1'],
                             'Gtp2T3Time': '3',
                             'Gtp2N3Attempts': '5',
                             'SessionRetries': 'false',
                             'Gtp2CustomMsgEn': 'false',
                             'HomeAddrType': home_addr_type,
                             'Gtp2AmbrDownlink': input_dict['apn1Details']['apn1DownlinkAmbr'],
                             'Gtp2AmbrUplink': input_dict['apn1Details']['apn1UplinkAmbr'],
                             'Gtp2QosClassId_1': input_dict['apn1Details']['apn1Qci'],
                             'Gtp2QosArpValue_1': input_dict['apn1Details']['apn1Pl'],
                             'Gtp2QosArpPreemptCapEn_1': input_dict['apn1Details']['apn1Pci'],
                             'Gtp2QosArpPreemptVulnEn_1': input_dict['apn1Details']['apn1Pvi'],
                             'Gtp2ApnTotalApns_0': '1',
                             'Gtp2Apn_0': input_dict['apn1Details']['apn1Name'],
                             'Gtp2ApnNumSpecifiedApns_0': '0',
                             'Gtp2IncTaiEn': 'true',
                             'Gtp2IncEcgiEn': 'true',
                             'Gtp2Tac': input_dict['enodeB1Details']['tac1'],
                             'Gtp2Ecgi': input_dict['enodeB1Details']['eCellId1'],
                             'Gtp2IncSaiEn': 'true',
                             'Gtp2IncRaiEn': 'false',
                             'Gtp2IncCgiEn': 'true',
                             'InitiateType': input_dict['initiateType'],
                             'MobilityTimeMs': input_dict['mobilityTimeline1Details']}
            # Configure Mobility Mode
            if "Single" in input_dict['handoffType']:
                gn_param_dict['MobilityMode'] = 'Single Handoff'
            else:
                gn_param_dict['MobilityMode'] = 'Continuous Handoff'
            # Configure Target node Gn Specific parameters based on RatType 3GS4 or 3GGn
            if "3GGn" in input_dict['scenario']:
                max_bitrate_uplink = self.calculate_max_bit_rate(input_dict[
                                                                     'apn1Details']['apn1UplinkMbr'])
                max_bitrate_downlink = self.calculate_max_bit_rate(input_dict[
                                                                       'apn1Details']['apn1DownlinkMbr'])

                if (max_bitrate_uplink is False or max_bitrate_downlink is False):
                    RobotLogger.log_logger.info(
                        "Calculated uplink_mbr values are not in the range: %s" % max_bitrate_uplink)
                    RobotLogger.log_logger.info(
                        "Calculated downlink_mbr values are not in the range: %s" % max_bitrate_downlink)
                else:
                    if (int(max_bitrate_uplink) >= 8700) and (int(max_bitrate_uplink) <= 256000):
                        temp_dict = {'QosIncGbruMbruExt_0_0': 'true',
                                     'QosMaxBitrateUplinkExt_0_0': max_bitrate_uplink}
                        gn_param_dict = {**gn_param_dict, **temp_dict}
                        del temp_dict
                    if (int(max_bitrate_downlink) >= 8700) and (int(max_bitrate_downlink) <= 256000):
                        temp_dict = {'QosIncGbrdMbrdExt_0_0': 'true',
                                     'QosMaxBitrateDownlinkExt_0_0': max_bitrate_downlink}
                        gn_param_dict = {**gn_param_dict, **temp_dict}
                        del temp_dict
                temp_dict = {'IncUli': 'true', 'UliMcc': input_dict['enodeB1Details']['mcc1'],
                             'UliMnc': input_dict['enodeB1Details']['mnc1'],
                             'SmApn_0': input_dict['apn1Details']['apn1Name'],
                             'QosTrafficPriority_0_0': input_dict['apn1Details'][
                                 'apn1TrafficHandlingPriority'],
                             'TrafficClass_0_0': input_dict['apn1Details'][
                                 'apn1TrafficClass'],
                             'UliLac': input_dict['enodeB1Details']['tac1'],
                             'UliCiSac': input_dict['enodeB1Details']['eCellId1']}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
            if "4G_3GS4" in input_dict['scenario']:
                if input_dict['initiateType'] == "LTE":
                    tgt_gtp2_radio_access_type = 1
                    gtp2_radio_access_type = 6
                else:
                    tgt_gtp2_radio_access_type = 6
                    gtp2_radio_access_type = 1

                temp_dict = {'TgtGtp2RadioAccessType': tgt_gtp2_radio_access_type,
                             'Gtp2RadioAccessType': gtp2_radio_access_type,
                             'TgtGtp2IncModApnAmbr': 'true',
                             'TgtGtp2AmbrDownlink': input_dict['apn1Details']['apn1DownlinkAmbr'],
                             'TgtGtp2AmbrUplink': input_dict['apn1Details']['apn1UplinkAmbr']}
                gn_param_dict = {**gn_param_dict, **temp_dict}
                del temp_dict
                # Configure SGW Reloccation
                if input_dict['sgwRelocation'] == "true":
                    # Enable SGW reloc flag
                    gn_param_dict['SgwRelocationEn'] = 'true'
                    # Configure SGW Mobility SUT - MobSgwSut & MobSgwUserSut
                else:
                    gn_param_dict['SgwRelocationEn'] = 'false'

            # Frame DMZ parameters for local host
            # traffic_enable = 1
            gn_param_dict['NetworkHost'] = "Local"
            gn_param_dict['NetworkHostNatedTrafficEn'] = "true"
            gn_param_dict['DataTraffic'] = "Continuous"

            # Enable dual stack configuration as required on Dmz node
            if home_addr_type == "3":
                gn_param_dict['DualStackEn'] = "true"
            else:
                gn_param_dict['DualStackEn'] = "false"
            # Configure the Gn landslide parameters
            ls_param = landslide_object.frame_landslide_parameters(
                conf_obj, gn_param_dict, tc_name, tc_type,
                node_index['gn_index'])
            if ls_param['Status'] is True:
                conf_obj = ls_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_landslide_parameters failed"}
            # Create PgwSut dictionary and assign in gn_param_dict
            pgw1_ip = input_dict['gw1Details']['pgw1Ip']
            pgw1_sut_name = pgw1_ip.replace(".", "_")
            # gn_param_dict['PgwV4Sut'] = pgw1_ip
            # RobotLogger.log_logger.info("Landslide Gn Parameters: %s" % (gn_param_dict))
            # Add SUT to the Landslide inventory
            # pgw1_add_sut = landslide_object.add_sut(ip_address=pgw1_ip, management_ip='1.2.3.4', sut_name=pgw1_sut_name)
            pgw1_add_sut = landslide_object.add_sut(pgw1_ip, '1.2.3.4', pgw1_sut_name)
            if pgw1_add_sut['Status'] is False:
                return {'Status': 'False', 'Error': "Failed to add PGW SUT to the LS inventory"}

            # Framing PGW sut details for Landslide Test Session
            pgw1_param = landslide_object.frame_sut_parameters(conf_obj, "PgwV4Sut", pgw1_sut_name,
                                                               node_index['gn_index'])
            if pgw1_param['Status'] is True:
                conf_obj = pgw1_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_sut_parameters for PGW failed"}

            # Create SGW SUT dictionary and assign in gn_param_dict
            sgw1_ip = input_dict['gw1Details']['sgw1Ip']
            sgw1_sut_name = sgw1_ip.replace(".", "_")
            # gn_param_dict['SgwSut'] = pgw1_ip
            # RobotLogger.log_logger.info("Landslide Gn Parameters: %s" % (gn_param_dict))

            # Add SUT to the Landslide inventory
            sgw1_add_sut = landslide_object.add_sut(ip_address=sgw1_ip,
                                                    management_ip='1.2.3.4',
                                                    sut_name=sgw1_sut_name)
            if sgw1_add_sut['Status'] is False:
                return {'Status': 'False', 'Error': "Failed to add SGW SUT to the LS inventory"}

            # Framing SGW sut details for Landslide Test Session
            sgw1_param = landslide_object.frame_sut_parameters(conf_obj,
                                                               "SgwSut", sgw1_sut_name,
                                                               node_index['gn_index'])
            if sgw1_param['Status'] is True:
                conf_obj = sgw1_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_sut_parameters for SGW failed"}

            # Create SGW-User SUT dictionary and assign to gn_param_dict
            sgw1_s1u_ip = input_dict['gw1Details']['sgw1S1uIp']
            sgw1_s1u_sut_name = sgw1_s1u_ip.replace(".", "_")
            # gn_param_dict['SgwSut'] = pgw1_ip
            # RobotLogger.log_logger.info("Landslide Gn Parameters: %s" % (gn_param_dict))

            # Add SUT to the Landslide inventory
            sgw1_s1u_add_sut = landslide_object.add_sut(ip_address=sgw1_s1u_ip,
                                                        management_ip='1.2.3.4',
                                                        sut_name=sgw1_s1u_sut_name)
            if sgw1_s1u_add_sut['Status'] is False:
                return {'Status': 'False', 'Error': "Failed to add SGW1-User  SUT to the LS inventory"}

            # Framing PGW sut details for Landslide Test Session
            sgw1_s1u_param = landslide_object.frame_sut_parameters(conf_obj, "SgwUserSut",
                                                                   sgw1_s1u_sut_name,
                                                                   node_index['gn_index'])
            if sgw1_s1u_param['Status'] is True:
                conf_obj = sgw1_s1u_param['conf_obj']
            else:
                return {'Status': 'False', 'Error': "frame_sut_parameters for SGW-S1U failed"}
            # Add SUT GGSN as PGW Sut for inter_rat scenarios involving 3GGn
            if "3GGn" in input_dict['scenario']:
                ggsn1_param = landslide_object.frame_sut_parameters(conf_obj, "SutGgsn",
                                                                    pgw1_sut_name,
                                                                    node_index['gn_index'])
                if ggsn1_param['Status'] is True:
                    conf_obj = ggsn1_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "frame_sut_parameters for SutGgsn failed"}
            # Add relocated SGW detail
            if input_dict['sgwRelocation'] == "true":
                # Create SGW SUT dictionary
                sgw2_ip = input_dict['gw2Details']['sgw2Ip']
                sgw2_sut_name = sgw2_ip.replace(".", "_")
                # Add SUT to the Landslide inventory
                sgw2_add_sut = landslide_object.add_sut(ip_address=sgw2_ip,
                                                        management_ip='1.2.3.4',
                                                        sut_name=sgw2_sut_name)
                if sgw2_add_sut['Status'] is False:
                    return {'Status': 'False', 'Error': "Failed to add SGW2 SUT to the LS inventory"}
                sgw2_param = landslide_object.frame_sut_parameters(conf_obj,
                                                                   "MobSgwSut",
                                                                   sgw2_sut_name,
                                                                   node_index['gn_index'])
                if sgw2_param['Status'] is True:
                    conf_obj = sgw2_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "frame_sut_parameters failed"}
                # Create SGW-User SUT dictionary
                sgw2_s1u_ip = input_dict['gw2Details']['sgw2S1uIp']
                sgw2_s1u_sut_name = sgw2_s1u_ip.replace(".", "_")
                # gn_param_dict['SgwSut'] = pgw1_ip
                # RobotLogger.log_logger.info("Landslide Gn Parameters: %s" % (gn_param_dict))

                # Add SUT to the Landslide inventory
                sgw2_s1u_add_sut = landslide_object.add_sut(ip_address=sgw2_s1u_ip,
                                                            management_ip='1.2.3.4',
                                                            sut_name=sgw2_s1u_sut_name)
                if sgw2_s1u_add_sut['Status'] is False:
                    return {'Status': 'False', 'Error': "Failed to add SGW1-User  SUT to the LS inventory"}

                # Framing PGW sut details for Landslide Test Session
                sgw2_s1u_param = landslide_object.frame_sut_parameters(conf_obj,
                                                                       "MobSgwUserSut",
                                                                       sgw2_s1u_sut_name, 0)
                if sgw2_s1u_param['Status'] is True:
                    conf_obj = sgw2_s1u_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "frame_sut_parameters failed"}
            # Node parameters configuration
            # Framing enodeB control address for Landslide Test Session
            enodeb1_node_param = landslide_object.frame_node_parameters(conf_obj, "EnbUserAddr",
                                                                        input_dict[
                                                                            'enodeB1Details'][
                                                                            'enodeB1Ip'],
                                                                        input_dict[
                                                                            'enodeB1Details'][
                                                                            'enodeB1GwIp'], 1,
                                                                        input_dict[
                                                                            'enodeB1Details'][
                                                                            'enodeB1PhyName'],
                                                                        1500, "",
                                                                        input_dict[
                                                                            'chassis1Details'][
                                                                            'gnVlan'],
                                                                        node_index['gn_index'])
            reserve_ports = reserve_ports + 1
            phy_eth = input_dict['enodeB1Details']['enodeB1PhyName'].replace("v6", "")
            phy_eth_names_list.append(phy_eth)
            RobotLogger.log_logger.info("Config enodeB details: %s" % (conf_obj))
            if enodeb1_node_param['Status'] is True:
                conf_obj = enodeb1_node_param['conf_obj']
                RobotLogger.log_logger.info("Config enodeB1 details: %s" % (conf_obj))
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure enodeB1 node parameters for the landslide test script"}

            # Framing MMEcontrol address for Landslide Test Session
            mme_node1_param = landslide_object.frame_node_parameters(conf_obj, "MmeControlAddr",
                                                                     input_dict['mme1Details'][
                                                                         'mme1Ip'],
                                                                     input_dict['mme1Details'][
                                                                         'mme1GwIp'], 1,
                                                                     input_dict['mme1Details'][
                                                                         'mme1PhyName'], 1500,
                                                                     input_dict['mme1Details'][
                                                                         'mme1PhyName'],
                                                                     input_dict['chassis1Details'][
                                                                         'gnVlan'],
                                                                     node_index['gn_index'])
            if mme_node1_param['Status'] is True:
                conf_obj = mme_node1_param['conf_obj']
                RobotLogger.log_logger.info("Config mme details: %s" % (conf_obj))
                RobotLogger.log_logger.info("Gn Parameters framed successfully")
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure mme node parameters for the landslide test script"}

            # Framing SGSN address for Landslide Test Session
            sgsn_node_param = landslide_object.frame_node_parameters(conf_obj, "SgsnCtlAddr",
                                                                     input_dict['sgsn1Details'][
                                                                         'sgsn1Ip'],
                                                                     input_dict['sgsn1Details'][
                                                                         'sgsn1GwIp'], 1,
                                                                     input_dict['sgsn1Details'][
                                                                         'sgsn1PhyName'], 1500,
                                                                     input_dict['sgsn1Details'][
                                                                         'sgsn1PhyName'],
                                                                     input_dict['chassis1Details'][
                                                                         'gnVlan'],
                                                                     node_index['gn_index'])
            reserve_ports = reserve_ports + 1
            if sgsn_node_param['Status'] is True:
                conf_obj = sgsn_node_param['conf_obj']
                RobotLogger.log_logger.info("Config sgsn details: %s" % (conf_obj))
                RobotLogger.log_logger.info("Gn Parameters framed successfully")
            else:
                return {'Status': 'False',
                        'Error': "Unable to configure sgsn node parameters for the landslide test script"}
            # Framing Dmz node parameters
            if home_addr_type == "3":
                dmz_v4_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "Ipv4NetworkHostAddrLocal",
                    input_dict['dmz1Details']['dmz1Ip'],
                    input_dict['dmz1Details']['dmz1GwIp'], "1",
                    input_dict['dmz1Details']['dmz1PhyName'], 1500,
                    "", input_dict['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_v4_node_param['Status'] is True:
                    conf_obj = dmz_v4_node_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "DMZv4 frame_node_parameters failed"}
                dmz_v6_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "Ipv6NetworkHostAddrLocal",
                    input_dict['dmz1Details']['dmz1Ipv6'],
                    input_dict['dmz1Details']['dmz1GwIpv6'], "1",
                    input_dict['dmz1Details']['dmz1PhyNamev6'], 1500,
                    "", input_dict['chassis1Details']['giVlan'],
                    node_index['gn_index'])
                if dmz_v6_node_param['Status'] is True:
                    conf_obj = dmz_v6_node_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "DMZv6 frame_node_parameters failed"}
            else:
                dmz_node_param = landslide_object.frame_node_parameters(
                    conf_obj, "NetworkHostAddrLocal",
                    input_dict['dmz1Details']['dmz1Ip'],
                    input_dict['dmz1Details']['dmz1GwIp'], "1",
                    input_dict['dmz1Details']['dmz1PhyName'], 1500,
                    "", input_dict['chassis1Details']['giVlan'],
                    node_index['gn_index'], 1)
                if dmz_node_param['Status'] is True:
                    conf_obj = dmz_node_param['conf_obj']
                else:
                    return {'Status': 'False', 'Error': "DMZ frame_node_parameters failed"}
            phy_eth = list(set(phy_eth_names_list))
            reserve_ports = reserve_ports + 1
            dmz_port = input_dict['dmz1Details']['dmz1PhyName'].replace("v6", "")
            phy_eth_names_list.append(dmz_port)
            phy_eth_names_list = list(set(phy_eth_names_list))
            total_ports = len(phy_eth_names_list)
            RobotLogger.log_logger.info(
                "Port Capture List: {}, Total ports count : {}".format(phy_eth_names_list, total_ports))
            # Enable port capture
            pc_param = landslide_object.frame_port_capture_parameters(
                conf_obj, total_ports, phy_eth_names_list, test_server_id,
                on_start=True)
            if pc_param['Status'] is True:
                conf_obj = pc_param['conf_obj']
            else:
                RobotLogger.log_logger.info("Failed to frame ports")
                return {'Status': 'False', 'Error': "frame_port_capture_parameters failed"}
            # Apply and Save the configuration
            conf_test_session = landslide_object.config_landslide_test_session(
                conf_obj, library_id, test_session_name)
            if conf_test_session['Status'] is True:
                delay_step = "2"
                # phy_list_str = ' '.join(phy_eth_names_list)
                return {'Status': 'True', 'Info': "Successfully Configured", 'trafficParameterList': "lib_id " + str(
                    library_id) + " tsname " + test_server_name + " delaystep " + delay_step + " logfilepath " + str(
                    log_path) + " dmz_port " + str(dmz_port) + " gn_port " + str(phy_eth[0]) + " home_address " + str(
                    home_address)}
            else:
                return {'Status': 'False', 'Error': "Configuration failed"}
        except TypeError:
            RobotLogger.log_logger.debug(
                "TypeError occurred while configuring iRAT scenario:%s" % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "TypeError occurred while configuring iRAT scenario"}
        except ValueError:
            RobotLogger.log_logger.debug(
                "ValueError occurred while configuring iRAT scenario:%s " % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "ValueError occurred while configuring iRAT scenario"}
        except IOError:
            RobotLogger.log_logger.debug(
                "IOError occurred while configuring iRAT scenario:%s " % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "IOError occurred while configuring iRAT scenario"}
        except Exception:
            RobotLogger.log_logger.debug(
                "Exception occurred while configuring iRAT scenario:%s" % (str(traceback.format_exc())))
            return {'Status': 'False', 'Error': "Exception occurred while configuring iRAT scenario"}
