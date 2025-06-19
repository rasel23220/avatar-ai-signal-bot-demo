import streamlit as st
import random

st.set_page_config(page_title="Avatar AI Signal Bot", layout="centered")
st.title("🤖 Avatar AI Future Signal Bot")
st.markdown("Predict your next avatar move based on current game status.")

def predict_action(health, energy, last_action, opponent_action):
    actions = []
    if health < 30:
        actions.append({"action": "retreat", "confidence": random.randint(80, 95), "expected_outcome": "Avoid damage and recover"})
    elif energy > 70 and opponent_action == "idle":
        actions.append({"action": "charge", "confidence": random.randint(75, 90), "expected_outcome": "Chance to surprise opponent"})
    else:
        actions.append({"action": "defend", "confidence": random.randint(60, 80), "expected_outcome": "Reduce incoming damage"})
    actions += [
        {"action": "hold_position", "confidence": random.randint(50,70), "expected_outcome": "Observe and wait"},
        {"action": "counter_attack", "confidence": random.randint(40,65), "expected_outcome": "Risky but can reverse the situation"}
    ]
    return sorted(actions, key=lambda x: x['confidence'], reverse=True)[:3]

health = st.slider("Health", 0, 100, 75)
energy = st.slider("Energy", 0, 100, 50)
last_action = st.selectbox("Last Action", ["idle", "charge", "defend", "retreat"])
opponent_action = st.selectbox("Opponent Action", ["idle", "charge", "defend", "retreat"])

if st.button("🔍 Predict Action"):
    for idx, r in enumerate(predict_action(health, energy, last_action, opponent_action), 1):
        st.write(f"**Signal {idx}:** {r['action']}")
        st.write(f"- Expected Outcome: {r['expected_outcome']}")
        st.write(f"- Confidence Score: {r['confidence']}%")
