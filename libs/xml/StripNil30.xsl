<?xml version="1.0" encoding="UTF-8"?>
<!-- Strip attribute nil from inbound NaXML files berryme@yahoo.com 8/30/2018 -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                exclude-result-prefixes="array fn map math xhtml xs err" version="3.0">
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
    <xsl:strip-space elements="*"/>
    <!-- TEMPLATE #1 -->
    <xsl:template match="node()|@*">
        <xsl:copy>
            <xsl:apply-templates select="node()|@*"/>
        </xsl:copy>
    </xsl:template>
    <!-- TEMPLATE #2 -->
    <!-- <xsl:template match="*[@xsi:nil = 'true']" /> -->
    <xsl:template match="@*">
        <xsl:if test="local-name()!='nil'">
            <xsl:copy/>
        </xsl:if>
    </xsl:template>
</xsl:stylesheet>
