//
//  CourseSearchCellView.h
//  Qcumber
//
//  Created by Chris Cooper on 12-01-03.
//  Copyright (c) 2012 Chris Cooper. All rights reserved.
//

#import <AppKit/AppKit.h>

@interface CourseSearchCellView : NSTableCellView

@property (weak) IBOutlet NSTextField *codeLabel;
@property (weak) IBOutlet NSTextField *titleLabel;
@property (weak) IBOutlet NSButton *favoriteButton;
@property (weak) IBOutlet NSTextField *descriptionLabel;
@property (weak) IBOutletCollection(NSTextField) NSArray *sectionTypeLabels;
@property (weak) IBOutlet NSTextField *creditsLabel;

@end
