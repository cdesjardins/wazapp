#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
	resource = "Symbian-2.6.61-443";
	domain ='s.whatsapp.net'
	whatsapp = WAXMPP(domain,resource,"phonenumber","jeanluis","encryptedIEMI");
	whatsapp.setReceiptAckCapable(True);

