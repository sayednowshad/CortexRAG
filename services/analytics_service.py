class AnalyticsService:

    @staticmethod
    def print_dashboard(
        analytics: dict
    ):

        print(
            "\n"
            + "=" * 60
        )

        print(
            "RAG PIPELINE DASHBOARD"
        )

        print(
            "=" * 60
        )

        for key, value in analytics.items():

            print(
                f"{key}: {value}"
            )

        print(
            "=" * 60
        )

    @staticmethod
    def print_failure(
        failure_type: str
    ):

        print(
            "\n"
            + "=" * 60
        )

        print(
            f"FAILURE: {failure_type}"
        )

        print(
            "=" * 60
        )