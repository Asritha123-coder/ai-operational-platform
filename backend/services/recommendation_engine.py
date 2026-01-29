def generate_recommendations(analysis, root_causes):
    recommendations = set()

    # Based on issue types
    if analysis.get("Login Issues", 0) > 0:
        recommendations.add(
            "Investigate authentication service and increase login retry monitoring"
        )

    if analysis.get("Performance Issues", 0) > 0:
        recommendations.add(
            "Analyze system latency and consider adding caching or load balancing"
        )

    if analysis.get("Database Issues", 0) > 0:
        recommendations.add(
            "Review database connection pool and optimize query performance"
        )

    # Based on root causes
    if root_causes.get("Authentication Service", 0) > 1:
        recommendations.add(
            "Scale authentication service horizontally to handle load"
        )

    if root_causes.get("Database", 0) > 0:
        recommendations.add(
            "Implement database failover and improve connection timeout handling"
        )

    return list(recommendations)
