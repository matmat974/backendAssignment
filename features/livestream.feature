

Feature: Livestream

  Scenario: Up a Livestream
    Given you already login
    When creating a livestream
    Then you need to execute the start livestream api
    And end the livestream