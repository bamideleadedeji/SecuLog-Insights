#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SecuLog Insights - Demonstration Script
"""

import sys
import os

# Add src to path
sys.path.append("src")

from data_cleaner import clean_security_logs
from threat_analyzer import ThreatAnalyzer

def main():
    print("=" * 50)
    print("SECULOG INSIGHTS - SECURITY ANALYSIS DEMO")
    print("=" * 50)
    
    # 1. Load and clean data
    print("\nSTEP 1: Loading and cleaning data...")
    df = clean_security_logs("data/sample_logs.csv")
    print(f"[OK] Loaded {len(df)} log entries")
    print(f"[OK] Columns: {', '.join(df.columns)}")
    
    # 2. Analyze threats
    print("\nSTEP 2: Analyzing threats...")
    analyzer = ThreatAnalyzer(df)
    results = analyzer.analyze()
    
    # 3. Display results
    print("\nSTEP 3: Security Assessment Results")
    print("-" * 40)
    
    summary = results["summary"]
    print(f"Total connections: {summary['total_connections']}")
    print(f"Attack attempts: {summary['attack_count']}")
    print(f"Attack percentage: {summary['attack_percentage']:.1f}%")
    
    attacks = results["attacks"]
    if attacks["status"] == "compromised":
        print(f"\n[ALERT] ATTACK DETECTED!")
        print(f"Attacker IP: {attacks['attacker_ip']}")
        print(f"Attack count: {attacks['attack_count']}")
        print(f"Target port: {attacks['target_port']}")
    
    # 4. Recommendations
    print("\nSTEP 4: Security Recommendations")
    print("-" * 40)
    for rec in results["recommendations"]:
        print(f"* {rec}")
    
    print("\n" + "=" * 50)
    print("[SUCCESS] ANALYSIS COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    main()
