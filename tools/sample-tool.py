#!/usr/bin/env python3
"""
AI-Powered Task Automation Tool
================================

A sample automation tool demonstrating best practices for AI-powered workflows.
This tool provides a foundation for building your own intelligent automation solutions.

Features:
- Configurable task scheduling
- AI integration for intelligent decisions
- Logging and error handling
- Modular and extensible design

Author: IknowAI Community
License: MIT
"""

import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('automation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class AutomationTool:
    """
    A flexible automation tool with AI capabilities.
    
    This class provides a framework for building intelligent automation
    workflows that can process data, make decisions, and execute actions.
    """
    
    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize the automation tool.
        
        Args:
            config_file: Path to configuration file
        """
        self.config = self._load_config(config_file)
        self.tasks_completed = 0
        self.tasks_failed = 0
        logger.info("Automation tool initialized")
    
    def _load_config(self, config_file: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_file: Path to config file
            
        Returns:
            Configuration dictionary
        """
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
            else:
                logger.warning(f"Config file {config_file} not found, using defaults")
                return self._get_default_config()
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict:
        """
        Get default configuration.
        
        Returns:
            Default configuration dictionary
        """
        return {
            "api_key": os.getenv('AI_API_KEY', ''),
            "model": "gpt-3.5-turbo",
            "max_retries": 3,
            "timeout": 30,
            "log_level": "INFO",
            "tasks": []
        }
    
    def analyze_data(self, data: str) -> Dict:
        """
        Analyze data using AI (placeholder for actual AI integration).
        
        Args:
            data: Input data to analyze
            
        Returns:
            Analysis results
        """
        logger.info(f"Analyzing data: {data[:50]}...")
        
        # Placeholder for AI analysis
        # In a real implementation, this would call an AI API
        result = {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "data_length": len(data),
            "summary": "Data analyzed successfully",
            "insights": [
                "Pattern detected",
                "No anomalies found",
                "Ready for processing"
            ]
        }
        
        return result
    
    def execute_task(self, task: Dict) -> bool:
        """
        Execute a single automation task.
        
        Args:
            task: Task configuration dictionary
            
        Returns:
            True if successful, False otherwise
        """
        try:
            task_name = task.get('name', 'Unnamed Task')
            logger.info(f"Executing task: {task_name}")
            
            # Get task parameters
            task_type = task.get('type', 'generic')
            task_data = task.get('data', '')
            
            # Process based on task type
            if task_type == 'analysis':
                result = self.analyze_data(task_data)
                logger.info(f"Analysis result: {result['summary']}")
            elif task_type == 'notification':
                self._send_notification(task_data)
            elif task_type == 'data_processing':
                self._process_data(task_data)
            else:
                logger.warning(f"Unknown task type: {task_type}")
            
            self.tasks_completed += 1
            logger.info(f"Task '{task_name}' completed successfully")
            return True
            
        except Exception as e:
            self.tasks_failed += 1
            logger.error(f"Task execution failed: {e}")
            return False
    
    def _send_notification(self, message: str):
        """
        Send a notification (placeholder implementation).
        
        Args:
            message: Notification message
        """
        logger.info(f"Notification: {message}")
        # In a real implementation, this could send emails, Slack messages, etc.
    
    def _process_data(self, data: str):
        """
        Process data (placeholder implementation).
        
        Args:
            data: Data to process
        """
        logger.info(f"Processing data: {len(data)} bytes")
        # Add your data processing logic here
    
    def run(self, tasks: Optional[List[Dict]] = None):
        """
        Run all configured tasks.
        
        Args:
            tasks: Optional list of tasks (uses config if not provided)
        """
        logger.info("Starting automation workflow")
        
        tasks_to_run = tasks or self.config.get('tasks', [])
        
        if not tasks_to_run:
            logger.warning("No tasks configured. Please add tasks to config.json")
            self._print_usage_example()
            return
        
        logger.info(f"Running {len(tasks_to_run)} tasks")
        
        for task in tasks_to_run:
            self.execute_task(task)
        
        # Print summary
        self._print_summary()
    
    def _print_summary(self):
        """
        Print execution summary.
        """
        total = self.tasks_completed + self.tasks_failed
        logger.info("\n" + "="*50)
        logger.info("AUTOMATION SUMMARY")
        logger.info("="*50)
        logger.info(f"Total tasks: {total}")
        logger.info(f"Completed: {self.tasks_completed}")
        logger.info(f"Failed: {self.tasks_failed}")
        logger.info(f"Success rate: {(self.tasks_completed/total*100):.1f}%" if total > 0 else "N/A")
        logger.info("="*50)
    
    def _print_usage_example(self):
        """
        Print usage example.
        """
        example_config = {
            "api_key": "your-api-key-here",
            "model": "gpt-3.5-turbo",
            "tasks": [
                {
                    "name": "Analyze Report",
                    "type": "analysis",
                    "data": "Sample data to analyze"
                },
                {
                    "name": "Send Notification",
                    "type": "notification",
                    "data": "Task completed successfully!"
                }
            ]
        }
        
        print("\n" + "="*50)
        print("EXAMPLE CONFIGURATION (save as config.json)")
        print("="*50)
        print(json.dumps(example_config, indent=2))
        print("="*50 + "\n")


def main():
    """
    Main entry point for the automation tool.
    """
    parser = argparse.ArgumentParser(
        description='AI-Powered Task Automation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python sample-tool.py                    # Run with default config
  python sample-tool.py --config my.json   # Run with custom config
  python sample-tool.py --demo             # Run demo mode
        """
    )
    
    parser.add_argument(
        '--config',
        default='config.json',
        help='Path to configuration file (default: config.json)'
    )
    
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run in demo mode with sample tasks'
    )
    
    args = parser.parse_args()
    
    # Initialize tool
    tool = AutomationTool(args.config)
    
    if args.demo:
        # Run demo tasks
        demo_tasks = [
            {
                "name": "Demo Analysis",
                "type": "analysis",
                "data": "This is sample data for demonstration purposes. " * 10
            },
            {
                "name": "Demo Notification",
                "type": "notification",
                "data": "Demo automation completed successfully!"
            }
        ]
        logger.info("Running in DEMO mode")
        tool.run(demo_tasks)
    else:
        # Run configured tasks
        tool.run()


if __name__ == "__main__":
    main()
