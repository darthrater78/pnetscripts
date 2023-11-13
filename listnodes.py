#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import os

def list_nodes_in_xml_lab(lab_file):
    if not os.path.getsize(lab_file):
        print(f"The file {lab_file} is empty.")
        return

    try:
        tree = ET.parse(lab_file)
        root = tree.getroot()

        nodes = root.findall('.//node')
        print(f"Found {len(nodes)} nodes.")  # Diagnostic print

        # Store node details in a list
        node_details = []
        for node in nodes:
            node_id = int(node.get('id'))  # Convert ID to integer for sorting
            node_name = node.get('name', 'Unknown')
            node_template = node.get('template', 'Unknown')  # Extract node template
            node_details.append((node_id, node_name, node_template))

        # Sort the nodes by ID
        node_details.sort(key=lambda x: x[0])

        # Print sorted nodes
        for node_id, node_name, node_template in node_details:
            print(f"Node ID: {node_id}, Name: {node_name}, Template: {node_template}")

    except Exception as e:
        print(f"Error reading {lab_file}: {e}")

def main():
    lab_file_path = '/opt/unetlab/labs/[name of your lab file].unl'  # Path to the specific lab file
    list_nodes_in_xml_lab(lab_file_path)

if __name__ == "__main__":
    main()
