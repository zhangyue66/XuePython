old_pcf = {
    "_id" : ObjectId("5e62b16d12169195bcf10ace"),
    "display_name" : "PCF",
    "epc_node_type" : "PCF",
    "description" : "Common PCF Schema to render the form dynamically",
    "sections_display_type" : "default",
    "target_collection_name" : "ANT_Groups",
    "sections" : {
        "pcf_cluster" : {
            "display_name" : "PCF Cluster Details",
            "description" : "",
            "container_type" : {
                "value" : "nonarray",
                "limit" : ""
            },
            "is_required" : true,
            "sub_sections" : {
                "elements" : {},
                "inner_sub_sections" : {
                    "elements" : {}
                }
            },
            "elements" : {
                "cluster_name" : {
                    "display_name" : "Cluster Name",
                    "description" : "",
                    "type" : "alphanumeric",
                    "data_type" : "string",
                    "possible_values" : [],
                    "default_value" : "",
                    "value" : "",
                    "is_editable" : true,
                    "show_field" : true,
                    "is_required" : true,
                    "load_another_schema" : false,
                    "input_device_model" : false,
                    "path" : "sections.pcf_cluster.elements.cluster_name",
                    "validation" : {
                        "regular_expression_pattern" : "^[A-z0-9_-\\s]+$",
                        "min_length" : "1",
                        "max_length" : "32"
                    },
                    "dependant_options" : {
                        "dependency" : {
                            "options" : [
                                {
                                    "name" : "",
                                    "value" : []
                                },
                                {
                                    "required_possible_value" : []
                                }
                            ]
                        },
                        "selected_values" : {}
                    },
                    "derivation_query" : [
                        {
                            "source" : "",
                            "output" : "",
                            "collection" : "",
                            "filter" : {},
                            "projection" : {}
                        }
                    ],
                    "target_collection_path" : "group_name"
                },
                "vendor" : {
                    "display_name" : "Vendor",
                    "description" : "",
                    "type" : "dropdown",
                    "data_type" : "string",
                    "possible_values" : [
                        "Cisco"
                    ],
                    "default_value" : "",
                    "value" : "",
                    "is_editable" : true,
                    "show_field" : true,
                    "is_required" : true,
                    "load_another_schema" : true,
                    "input_device_model" : true,
                    "path" : "sections.pcf_cluster.elements.vendor",
                    "validation" : {
                        "regular_expression_pattern" : "",
                        "min_length" : "",
                        "max_length" : ""
                    },
                    "dependant_options" : {
                        "dependency" : {
                            "options" : [
                                {
                                    "name" : "",
                                    "value" : []
                                },
                                {
                                    "required_possible_value" : []
                                }
                            ]
                        },
                        "selected_values" : {}
                    },
                    "derivation_query" : [
                        {
                            "source" : "",
                            "output" : "",
                            "collection" : "",
                            "filter" : {},
                            "projection" : {}
                        }
                    ],
                    "target_collection_path" : "vendor"
                },
                "device_type" : {
                    "display_name" : "Device Type",
                    "description" : "",
                    "type" : "dropdown",
                    "data_type" : "string",
                    "possible_values" : [
                        "CPS"
                    ],
                    "default_value" : "",
                    "value" : "",
                    "is_editable" : true,
                    "show_field" : false,
                    "is_required" : true,
                    "load_another_schema" : true,
                    "input_device_model" : true,
                    "path" : "sections.pcf_cluster.elements.device_type",
                    "validation" : {
                        "regular_expression_pattern" : "",
                        "min_length" : "",
                        "max_length" : ""
                    },
                    "dependant_options" : {
                        "dependency" : {
                            "options" : [
                                {
                                    "name" : "sections.pcf_cluster.elements.vendor",
                                    "value" : [
                                        "Cisco"
                                    ]
                                },
                                {
                                    "required_possible_value" : [
                                        "CPS"
                                    ]
                                }
                            ]
                        },
                        "selected_values" : {}
                    },
                    "derivation_query" : [
                        {
                            "source" : "",
                            "output" : "",
                            "collection" : "",
                            "filter" : {},
                            "projection" : {}
                        }
                    ],
                    "target_collection_path" : "device_type"
                },
                "deployment_mode" : {
                    "display_name" : "Deployment Mode",
                    "description" : "",
                    "type" : "dropdown",
                    "data_type" : "string",
                    "possible_values" : [],
                    "default_value" : "",
                    "value" : "",
                    "is_editable" : false,
                    "show_field" : true,
                    "is_required" : true,
                    "load_another_schema" : true,
                    "input_device_model" : true,
                    "path" : "sections.pcf_cluster.elements.deployment_mode",
                    "validation" : {
                        "regular_expression_pattern" : "",
                        "min_length" : "",
                        "max_length" : ""
                    },
                    "dependant_options" : {
                        "dependency" : {
                            "options" : [
                                {
                                    "name" : "",
                                    "value" : []
                                },
                                {
                                    "required_possible_value" : []
                                }
                            ]
                        },
                        "selected_values" : {}
                    },
                    "derivation_query" : [
                        {
                            "source" : "inventory",
                            "output" : "UI",
                            "collection" : "ANT_NetworkInventory_Schema",
                            "filter" : {
                                "projects__displayName" : "Zone Management"
                            },
                            "projection" : {
                                "_id" : 0,
                                "projects__possibleValues__value" : 1
                            }
                        }
                    ],
                    "target_collection_path" : "deployment_mode"
                }
            }
        }
    },
    "device_model_matrix" : [
        {
            "vendor" : [
                "Cisco"
            ],
            "device_type" : [
                "CPS"
            ],
            "deployment_mode" : [
                "NorthRim"
            ],
            "device_model_type" : "Cisco_CPS_NorthRim_PCF",
            "device_display_type" : "default",
            "no_of_devices" : 1
        }
    ]
}