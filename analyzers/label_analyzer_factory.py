from analyzers.aa8.ak3_atnt_barcode_labels import *
from analyzers.aa8.ak3_au_tw_sg_barcode_labels import *
from analyzers.aa8.ak3_emea_barcode_labels import *
from analyzers.aa8.ak3_gstore_ca_barcode_labels import *
from analyzers.aa8.ak3_in_barcode_labels import *
from analyzers.aa8.ak3_in_text_labels import *
from analyzers.aa8.ak3_jp_barcode_labels import *
from analyzers.aa8.ak3_tmo_barcode_labels import *
from analyzers.aa8.ak3_vzw_barcode_labels import *
from analyzers.aa8.tg4_apac_barcode_labels import *
from analyzers.aa8.tg4_atnt_barcode_labels import *
from analyzers.aa8.tg4_emea_barcode_labels import *
from analyzers.aa8.tg4_gstore_barcode_labels import *
from analyzers.aa8.tg4_in_barcode_labels import *
from analyzers.aa8.tg4_in_text_labels import *
from analyzers.aa8.tg4_jp_barcode_labels import *
from analyzers.aa8.tg4_tmo_barcode_labels import *
from analyzers.aa8.tg4_vzw_barcode_labels import *


class LabelAnalyzerFactory:
    """
    Factory class to create the appropriate label analyzer based on SKU name.
    Uses a class registration pattern to avoid creating unnecessary instances.
    """
    def __init__(self):
        """
        Initialize the factory and register all available analyzers.
        """
        # Dictionary to store registered analyzer classes by type
        self._registry = {
            'barcode': [],
            'text': []
        }
        
        # Register all analyzers upon initialization
        self._register_all()
    
    def _register(self, analyzer_class, analyzer_type='barcode'):
        """
        Register an analyzer class with its SKU pattern.
        
        Args:
            analyzer_class: The analyzer class to register
            analyzer_type: The type of analyzer ('barcode' or 'text')
        """
        # Create a temporary instance and add it to registry if it has sku_name
        instance = analyzer_class()
        if hasattr(instance, 'sku_name'):
            self._registry[analyzer_type].append((instance.sku_name, analyzer_class))
    
    def _register_all(self):
        """
        Register all available analyzer classes.
        This is called automatically during initialization.
        """
        # Register AK3 barcode analyzers
        self._register(AK3_US_VZW_CL1_Retail_Label)
        self._register(AK3_US_VZW_CL2_Retail_Label)
        self._register(AK3_US_VZW_CL3_Retail_Label)
        self._register(AK3_US_VZW_CL4_Retail_Label)
        self._register(AK3_US_TMO_CL1_128G_Retail_Label)
        self._register(AK3_US_TMO_CL1_128G_Demo_Retail_Label)
        self._register(AK3_US_TMO_CL2_Retail_Label)
        self._register(AK3_US_TMO_CL3_Retail_Label)
        self._register(AK3_US_TMO_CL3_Demo_Retail_Label)
        self._register(AK3_US_TMO_CL4_Retail_Label)
        self._register(AK3_US_TMO_CL1_256G_Retail_Label)
        self._register(AK3_US_ATnT_CL1_Retail_Label)
        self._register(AK3_US_ATnT_CL1_Demo_Retail_Label)
        self._register(AK3_US_GSTORE_CA_CL1_Retail_Label)
        self._register(AK3_US_GSTORE_CA_CL1_Demo_Retail_Label)
        self._register(AK3_US_GSTORE_CA_CL3_Demo_Retail_Label)
        self._register(AK3_US_GSTORE_CA_CL2_Retail_Label)
        self._register(AK3_US_GSTORE_CA_CL3_Retail_Label)
        self._register(AK3_US_GSTORE_CA_CL4_Retail_Label)
        self._register(AK3_EMEA_CL1_Retail_Label)
        self._register(AK3_EMEA_CL1_Demo_Retail_Label)
        self._register(AK3_EMEA_CL2_Retail_Label)
        self._register(AK3_EMEA_CL3_Retail_Label)
        self._register(AK3_EMEA_CL3_Demo_Retail_Label)
        self._register(AK3_EMEA_CL4_Retail_Label)
        self._register(AK3_AU_TW_SG_CL1_Retail_Label)
        self._register(AK3_AU_TW_SG_CL1_Demo_Retail_Label)
        self._register(AK3_AU_TW_SG_CL2_Retail_Label)
        self._register(AK3_AU_TW_SG_CL3_Retail_Label)
        self._register(AK3_AU_TW_SG_CL3_Demo_Retail_Label)
        self._register(AK3_AU_TW_SG_CL4_Retail_Label)
        self._register(AK3_IN_CL1_Retail_Label)
        self._register(AK3_IN_CL1_Demo_Retail_Label)
        self._register(AK3_IN_CL2_Retail_Label)
        self._register(AK3_IN_CL3_Retail_Label)
        self._register(AK3_IN_CL3_Demo_Retail_Label)
        self._register(AK3_IN_CL4_Retail_Label)
        self._register(AK3_JP_CL1_Retail_Label)
        self._register(AK3_JP_CL1_Demo_Retail_Label)
        self._register(AK3_JP_CL2_Retail_Label)
        self._register(AK3_JP_CL3_Retail_Label)
        self._register(AK3_JP_CL3_Demo_Retail_Label)
        self._register(AK3_JP_CL4_Retail_Label)

        # Register TG4 barcode analyzers
        self._register(TG4_US_VZW_Retail_Label)
        self._register(TG4_GSTORE_Retail_Label)
        self._register(TG4_IN_Retail_Label)
        self._register(TG4_APAC_Retail_Label)
        self._register(TG4_JP_Retail_Label)
        self._register(TG4_EMEA_Retail_Label)
        self._register(TG4_CLR1_128GB_TMO_Retail_Label)
        self._register(TG4_CLR1_256GB_TMO_Retail_Label)
        self._register(TG4_CLR2_TMO_Retail_Label)
        self._register(TG4_CLR3_TMO_Retail_Label)
        self._register(TG4_CLR4_TMO_Retail_Label)
        self._register(TG4_CLR1_128_ATT_Retail_Label)
        self._register(TG4_CLR2_128_ATT_Retail_Label)
        self._register(TG4_CLR3_128_ATT_Retail_Label)
        self._register(TG4_DEMO_CLR1_128_ATT_Retail_Label)
        self._register(TG4_DEMO_CLR3_128_ATT_Retail_Label)
        self._register(TG4_DEMO_CLR1_TMO_Retail_Label)
        self._register(TG4_DEMO_CLR1_TMO_HQ_Units_Retail_Label)
        self._register(TG4_DEMO_CLR3_TMO_Retail_Label)
        self._register(TG4_DEMO_GSTORE_Retail_Label)
        self._register(TG4_DEMO_EMEA_Retail_Label)
        self._register(TG4_DEMO_APAC_Retail_Label)
        self._register(TG4_DEMO_IN_Retail_Label)
        self._register(TG4_DEMO_JP_Retail_Label)

        # Register text analyzers
        self._register(AK3_IN_MRP_128G_TEXT_Label, 'text')
        self._register(AK3_IN_MRP_256G_TEXT_Label, 'text')
        self._register(TG4_IN_MRP_TEXT_Label, 'text')

    def create_analyzer(self, type, sku_name):
        """
        Create and return an appropriate label analyzer instance based on the SKU name.

        Args:
            type: The type of analyzer ('barcode' or 'text')
            sku_name: The SKU name to match

        Returns:
            An instance of an appropriate label analyzer or None if no match is found
        """
        # Ensure we have classes registered for the requested type
        if type not in self._registry:
            return None
            
        # Check if the SKU name matches any of the registered patterns
        for patterns, analyzer_class in self._registry[type]:
            # Check if sku_name matches any pattern in the analyzer's sku_name list
            for pattern_list in patterns:
                # Check if pattern_list is a list/tuple and if sku_name matches any element
                if isinstance(pattern_list, (list, tuple)) and any(sku_name in pattern for pattern in pattern_list):
                    return analyzer_class()
                # Or check if sku_name is in the pattern directly
                elif sku_name in pattern_list:
                    return analyzer_class()
                
        # No match found
        return None


# Example usage:
# factory = LabelAnalyzerFactory()
# analyzer = factory.create_analyzer('barcode', 'AK3_US_VZW_CL1')
