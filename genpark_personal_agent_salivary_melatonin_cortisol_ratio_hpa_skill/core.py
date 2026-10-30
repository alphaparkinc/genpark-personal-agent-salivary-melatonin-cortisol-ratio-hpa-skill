# -*- coding: utf-8 -*-
"""Salivary Melatonin-Cortisol Ratio Sentinel for GenPark Personal Agent."""
import json
from typing import Dict, Any

class SalivaryMelatoninCortisolRatioSentinel:
    @staticmethod
    def calculate_melatonin_cortisol_ratio(evening_melatonin_pg_ml: float, evening_cortisol_nmol_l: float) -> Dict[str, Any]:
        # Cortisol (nmol/L) to pg/mL conversion factor ~ 362.5
        cortisol_pg_ml = evening_cortisol_nmol_l * 362.5
        mcr = round(evening_melatonin_pg_ml / max(1.0, cortisol_pg_ml), 4)
        
        if mcr >= 0.04:
            tier = "OPTIMAL_CIRCADIAN_PINEAL_DOMINANCE"
            readiness = "Strong nocturnal sleep drive; cortisol successfully suppressed by SCN."
        elif mcr >= 0.015:
            tier = "MILD_NOCTURNAL_HPA_HYPERAROUSAL"
            readiness = "Elevated evening cortisol causing sleep-onset latency prolongation and fragmented REM."
        else:
            tier = "INVERTED_STRESS_CYCLE_BURNOUT"
            readiness = "Critical circadian inversion: hypercortisolemia suppressing pineal melatonin output."

        return {
            "salivary_melatonin_pg_ml": evening_melatonin_pg_ml,
            "salivary_cortisol_nmol_l": evening_cortisol_nmol_l,
            "melatonin_cortisol_ratio": mcr,
            "biological_sleep_readiness": tier,
            "clinical_interpretation": readiness
        }

    @staticmethod
    def assess_hpa_circadian_exhaustion_stage(car_morning_cortisol_nmol_l: float, bedtime_cortisol_nmol_l: float, noon_cortisol_nmol_l: float = 12.0) -> Dict[str, Any]:
        # Healthy reference: Morning 18-30 nmol/L, Bedtime < 4 nmol/L
        if car_morning_cortisol_nmol_l > 35.0 and bedtime_cortisol_nmol_l > 6.0:
            stage = "STAGE_1_WIRED_AND_TIRED_ALARM"
            remedy = "Ashwagandha (KSM-66 600mg) and Phosphatidylserine (300mg before dinner) to downregulate ACTH."
        elif car_morning_cortisol_nmol_l < 12.0 and bedtime_cortisol_nmol_l > 6.0:
            stage = "STAGE_2_CIRCADIAN_INVERSION"
            remedy = "Morning bright light box (10,000 lux for 30m upon waking); absolute screen curfew at 21:00."
        elif car_morning_cortisol_nmol_l < 10.0 and bedtime_cortisol_nmol_l < 3.0:
            stage = "STAGE_3_HPA_ADRENAL_EXHAUSTION"
            remedy = "Rhodiola rosea (3% rosavins), Licorice root extract (glycyrrhizin), and adrenal cortex peptides."
        else:
            stage = "HEALTHY_EUSTRESS_DIURNAL_CURVE"
            remedy = "Maintain current work-rest lifestyle balance."

        return {
            "morning_cortisol_nmol_l": car_morning_cortisol_nmol_l,
            "bedtime_cortisol_nmol_l": bedtime_cortisol_nmol_l,
            "hpa_axis_functional_stage": stage,
            "recommended_phytotherapy": remedy
        }
