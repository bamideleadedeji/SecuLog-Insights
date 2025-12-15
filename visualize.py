#!/usr/bin/env python
# Simple visualization for attack patterns

import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')

from data_cleaner import clean_security_logs

def create_attack_visualization():
    # Load data
    df = clean_security_logs('data/sample_logs.csv')
    
    # Calculate attack stats
    total = len(df)
    attacks = len(df[df['action'] == 'DENY'])
    legitimate = total - attacks
    
    # Create pie chart
    labels = ['Legitimate Traffic', 'Attack Traffic']
    sizes = [legitimate, attacks]
    colors = ['lightgreen', 'red']
    
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Network Traffic Analysis: Attacks vs Legitimate')
    plt.axis('equal')
    
    # Save to outputs folder
    import os
    os.makedirs('outputs', exist_ok=True)
    plt.savefig('outputs/traffic_analysis.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"Visualization saved to outputs/traffic_analysis.png")
    print(f"Stats: {attacks}/{total} attacks ({attacks/total*100:.1f}%)")

if __name__ == "__main__":
    create_attack_visualization()
