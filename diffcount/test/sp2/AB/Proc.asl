/**************************************************************************
 *  ��Ȩ���� (C)2002������������ͨѶ�ɷ����޹�˾��
 *
 *  �ļ����ƣ�   mcs_app_PduInfo_Proc.asl
 *  �ļ���ʶ��
 *  ����ժҪ��   A���ڱ��浱ǰ�˿ڴ����pdu��fQueue�����Ϣ
 *  ����˵����   
 *  ��ǰ�汾��   0.5
 *  ���ߣ�       zhangmeifeng
 *  ������ڣ�
 *  �޸ļ�¼��
 **************************************************************************/
 
 // Standard include file
#include <policeApp600.h>
//#include "mcs_app_ipras.h"
//unsigned rtn_index               result[0:3];


script mcs_app_PduInfo_Proc
{ 
    rtn_index = 0xFF;
    if(PDU_INFO_MOD == opEntryType)
    {
        if(0 == pdu_portno)
        {
            flag_flowid0    = flag_flowid1;
            ras_pdu_index0  = ras_pdu_index;
        }
        else if(1 == pdu_portno)
        {
            flag_flowid1    = flag_flowiddd;
            ras_pdu_index1  = ras_pdu_indexddd;
        }
        else if(2 == pdu_portno)
        {
        }
        else if(3 == pdu_portno)
        {
            flag_flowid3    = flag_flowid;
            ras_pdu_index3  = ras_pdu_index;
        }
        else
        {
            flag_flowid4    = flag_flowid;
            ras_pdu_index4  = ras_pdu_index;
        }
    }
    if(0 == pdu_portno)
        rtn_index = (flag_flowid0 | (ras_pdu_index0 << 16));
    else if(1 == pdu_portno)
        rtn_index = (flag_flowid1 | (ras_pdu_index1 << 16));
			    else if(2 == pdu_portno)
			        rtn_index = (flag_flowid2 | (ras_pdu_index2 << 16));
			    else if(3 == pdu_portno)
			        rtn_index = (flag_flowid3 | (ras_pdu_index3 << 16));
			    else
			        rtn_index = (flag_flowid4 | (ras_pdu_index4 << 16));
}
